#!/usr/bin/env python3
"""
montador.py — Montador do JSON final para o QuestBank.

O agente Antigravity produz um arquivo intermediário enxuto (rascunho.json)
com apenas os campos que exigem inteligência. Este script cuida de toda a
parte mecânica:

  - Gera os IDs sequenciais (regular e A-prefixo para adaptada)
  - Copia os campos idênticos da regular para a adaptada
  - Preenche campos fixos: imagens, usedInExams, resolucao_link, created_at
  - Intercala regular + adaptada no array final
  - Valida o rascunho e aponta erros antes de gerar o JSON

Uso:
    python montador.py --id-inicial 000052
    python montador.py --id-inicial 000052 --rascunho saida/rascunho.json
    python montador.py --id-inicial 000052 --saida saida/questoes_exportadas.json
"""

import json
import sys
import argparse
import datetime
from pathlib import Path


# ── Campos copiados da questão regular para a adaptada sem alteração ──────────

CAMPOS_IDENTICOS = [
    "tipo",
    "disciplina",
    "topico",
    "conteudo",
    "assunto",
    "banca",
    "ano",
    "dificuldade",
    "resolucao_link",
    "imagens",
    "usedInExams",
    "created_at",
]

# ── Campos fixos (sempre o mesmo valor independente da questão) ───────────────

CAMPOS_FIXOS = {
    "imagens": [],
    "usedInExams": [],
    "resolucao_link": "",
}


# ── Helpers ───────────────────────────────────────────────────────────────────

def formatar_id(numero: int, largura: int) -> str:
    """Formata o número como string com zeros à esquerda."""
    return str(numero).zfill(largura)


def id_adaptada(id_regular: str) -> str:
    return f"A-{id_regular}"


def timestamp_agora() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"


def validar_rascunho(questoes: list) -> list[str]:
    """Retorna lista de erros encontrados no rascunho."""
    erros = []
    obrigatorios_regular = [
        "enunciado", "tipo", "disciplina", "topico", "conteudo",
        "assunto", "banca", "ano", "dificuldade", "gabarito", "alternativas",
    ]
    obrigatorios_adaptada = [
        "enunciado_adaptado", "alternativas_adaptadas", "gabarito_adaptado",
    ]
    tipos_validos = {"objetiva", "discursiva"}
    difs_validas = {"facil", "medio", "dificil"}

    for i, q in enumerate(questoes, start=1):
        prefixo = f"Questão #{i}"

        for campo in obrigatorios_regular:
            if campo not in q:
                erros.append(f"{prefixo}: campo obrigatório ausente → '{campo}'")

        for campo in obrigatorios_adaptada:
            if campo not in q:
                erros.append(f"{prefixo}: campo adaptado ausente → '{campo}'")

        tipo = q.get("tipo", "")
        if tipo and tipo not in tipos_validos:
            erros.append(f"{prefixo}: 'tipo' inválido → '{tipo}' (use 'objetiva' ou 'discursiva')")

        dif = q.get("dificuldade", "")
        if dif and dif not in difs_validas:
            erros.append(f"{prefixo}: 'dificuldade' inválida → '{dif}' (use 'facil', 'medio' ou 'dificil')")

        if tipo == "objetiva":
            alts = q.get("alternativas", [])
            if len(alts) < 2:
                erros.append(f"{prefixo}: questão objetiva precisa de ao menos 2 alternativas")
            alts_ad = q.get("alternativas_adaptadas", [])
            if len(alts_ad) != 3:
                erros.append(f"{prefixo}: versão adaptada deve ter exatamente 3 alternativas (tem {len(alts_ad)})")

        if tipo == "discursiva":
            alts = q.get("alternativas", [])
            if len(alts) != 0:
                erros.append(f"{prefixo}: questão discursiva não deve ter alternativas (tem {len(alts)})")
            alts_ad = q.get("alternativas_adaptadas", [])
            if len(alts_ad) != 0:
                erros.append(f"{prefixo}: questão discursiva adaptada não deve ter alternativas (tem {len(alts_ad)})")

    return erros


# ── Montagem ──────────────────────────────────────────────────────────────────

def montar_regular(rascunho: dict, id_str: str, ts: str) -> dict:
    """Constrói o objeto completo da questão regular."""
    q = {
        "id": id_str,
        "enunciado": rascunho["enunciado"],
        "tipo": rascunho["tipo"],
        "disciplina": rascunho["disciplina"],
        "topico": rascunho["topico"],
        "conteudo": rascunho["conteudo"],
        "assunto": rascunho["assunto"],
        "banca": rascunho["banca"],
        "ano": rascunho["ano"],
        "dificuldade": rascunho["dificuldade"],
        "gabarito": rascunho["gabarito"],
        "alternativas": rascunho.get("alternativas", []),
        **CAMPOS_FIXOS,
        "created_at": ts,
    }
    return q


def montar_adaptada(rascunho: dict, regular: dict, ts: str) -> dict:
    """Constrói o objeto completo da questão adaptada copiando campos da regular."""
    adaptada = {"id": id_adaptada(regular["id"])}

    # Campos idênticos: copiados da regular já montada
    for campo in CAMPOS_IDENTICOS:
        adaptada[campo] = regular[campo]

    # Campos que mudam
    adaptada["enunciado"]    = rascunho["enunciado_adaptado"]
    adaptada["alternativas"] = rascunho.get("alternativas_adaptadas", [])
    adaptada["gabarito"]     = rascunho["gabarito_adaptado"]

    # Campos fixos (garantia)
    adaptada.update(CAMPOS_FIXOS)
    adaptada["created_at"] = ts

    return adaptada


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Montador do JSON QuestBank")
    parser.add_argument(
        "--id-inicial", required=True,
        help="ID numérico inicial para a primeira questão. Ex: 000052"
    )
    parser.add_argument(
        "--rascunho", default="saida/rascunho.json",
        help="Caminho do rascunho gerado pelo agente (padrão: saida/rascunho.json)"
    )
    parser.add_argument(
        "--saida", default="saida/questoes_exportadas.json",
        help="Caminho do JSON final (padrão: saida/questoes_exportadas.json)"
    )
    args = parser.parse_args()

    # ── Lê rascunho ──────────────────────────────────────────────────────────
    caminho_rascunho = Path(args.rascunho)
    if not caminho_rascunho.exists():
        print(f"[ERRO] Rascunho não encontrado: {caminho_rascunho}")
        sys.exit(1)

    with open(caminho_rascunho, encoding="utf-8") as f:
        rascunho_data = json.load(f)

    questoes_rascunho = rascunho_data if isinstance(rascunho_data, list) else rascunho_data.get("questoes", [])

    if not questoes_rascunho:
        print("[ERRO] Nenhuma questão encontrada no rascunho.")
        sys.exit(1)

    # ── Valida ────────────────────────────────────────────────────────────────
    erros = validar_rascunho(questoes_rascunho)
    if erros:
        print(f"[ERRO] O rascunho contém {len(erros)} problema(s):\n")
        for e in erros:
            print(f"  • {e}")
        print("\nCorrija o rascunho e execute novamente.")
        sys.exit(1)

    # ── Determina largura do ID ───────────────────────────────────────────────
    id_inicial_str = args.id_inicial.lstrip("0") or "0"
    id_inicial_num = int(id_inicial_str)
    largura_id     = max(len(args.id_inicial), 5)

    # ── Monta questões ────────────────────────────────────────────────────────
    questoes_finais = []
    ts = timestamp_agora()

    for i, rascunho in enumerate(questoes_rascunho):
        id_str  = formatar_id(id_inicial_num + i, largura_id)
        regular = montar_regular(rascunho, id_str, ts)
        adaptada = montar_adaptada(rascunho, regular, ts)
        questoes_finais.append(regular)
        questoes_finais.append(adaptada)

    # ── Salva JSON final ──────────────────────────────────────────────────────
    caminho_saida = Path(args.saida)
    caminho_saida.parent.mkdir(parents=True, exist_ok=True)

    output = {"version": "1.0", "questions": questoes_finais}
    with open(caminho_saida, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    total_q   = len(questoes_rascunho)
    total_out = len(questoes_finais)
    print(f"[montador] Concluído.")
    print(f"  Questões no rascunho : {total_q}")
    print(f"  Questões no JSON     : {total_out} ({total_q} regulares + {total_q} adaptadas)")
    print(f"  IDs gerados          : {formatar_id(id_inicial_num, largura_id)} → {formatar_id(id_inicial_num + total_q - 1, largura_id)}")
    print(f"  Arquivo de saída     : {caminho_saida}")


if __name__ == "__main__":
    main()
