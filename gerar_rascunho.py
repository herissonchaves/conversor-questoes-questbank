import json
import re

def process_questions():
    questions = [
        {
            "enunciado": """<p style="text-align:justify;"><b>(UERJ - 2025)</b> Um dos animais de maior massa já identificados no planeta Terra é a baleia-azul. Admita que uma baleia dessa espécie tenha massa de 90 toneladas e volume de $86{,}5\,\text{m}^3$. <b>A densidade dessa baleia, em $\text{g/cm}^3$, é aproximadamente:</b></p>""",
            "tipo": "objetiva",
            "disciplina": "Física",
            "topico": "Mecânica",
            "conteudo": "Estática dos Fluidos",
            "assunto": "Densidade",
            "banca": "UERJ",
            "ano": 2025,
            "dificuldade": "facil",
            "gabarito": "B",
            "alternativas": [
                { "letra": "A", "texto": "$1{,}36$" },
                { "letra": "B", "texto": "$1{,}04$" },
                { "letra": "C", "texto": "$0{,}95$" },
                { "letra": "D", "texto": "$0{,}88$" }
            ],
            "enunciado_adaptado": """<div style="text-align: justify;"><span style="font-size: 0.875rem;"><b>(UERJ - 2025)</b> Uma baleia-azul tem massa de 90 toneladas e volume de $86{,}5\,\text{m}^3$.</span></div><p><b>Qual é o valor aproximado da densidade dessa baleia em $\text{g/cm}^3$?</b></p>""",
            "alternativas_adaptadas": [
                { "letra": "A", "texto": "$1{,}04$" },
                { "letra": "B", "texto": "$1{,}36$" },
                { "letra": "C", "texto": "$0{,}88$" }
            ],
            "gabarito_adaptado": "A"
        },
        {
            "enunciado": """<p style="text-align:justify;"><b>(UFPR - 2024)</b> Uma plataforma plana horizontal tem uma área $A$. Sobre ela, é colocado um objeto de massa $m$ constante, que fica estático no local, sujeito apenas à força gravitacional e à força exercida pela plataforma. As forças envolvidas no problema são todas orientadas perpendicularmente à plataforma. O objeto exerce uma pressão de valor $p = 2{,}0 \times 10^4\,\text{Pa}$ sobre a plataforma, e a massa do objeto vale $m = 600\,\text{g}$.</p><p style="text-align:justify;"><b>Considerando as informações apresentadas, assinale a alternativa que apresenta corretamente o valor da área $A$ da plataforma.</b></p><p style="text-align:justify;"><b>Dado:</b> $g = 10\,\text{m/s}^2$.</p>""",
            "tipo": "objetiva",
            "disciplina": "Física",
            "topico": "Mecânica",
            "conteudo": "Estática dos Fluidos",
            "assunto": "Pressão",
            "banca": "UFPR",
            "ano": 2024,
            "dificuldade": "medio",
            "gabarito": "A",
            "alternativas": [
                { "letra": "A", "texto": "$A = 3{,}0 \times 10^{-4}\,\text{m}^2$" },
                { "letra": "B", "texto": "$A = 6{,}0 \times 10^{-4}\,\text{m}^2$" },
                { "letra": "C", "texto": "$A = 3{,}0 \times 10^{-5}\,\text{m}^2$" },
                { "letra": "D", "texto": "$A = 6{,}0 \times 10^{-5}\,\text{m}^2$" },
                { "letra": "E", "texto": "$A = 3{,}0 \times 10^{-6}\,\text{m}^2$" }
            ],
            "enunciado_adaptado": """<div style="text-align: justify;"><span style="font-size: 0.875rem;"><b>(UFPR - 2024)</b> Uma plataforma suporta um objeto de massa $600\,\text{g}$. A pressão exercida pelo objeto na plataforma é de $p = 2{,}0 \times 10^4\,\text{Pa}$. Considere a gravidade $g = 10\,\text{m/s}^2$.</span></div><p><b>Qual é o valor da área $A$ da plataforma?</b></p>""",
            "alternativas_adaptadas": [
                { "letra": "A", "texto": "$3{,}0 \times 10^{-5}\,\text{m}^2$" },
                { "letra": "B", "texto": "$3{,}0 \times 10^{-4}\,\text{m}^2$" },
                { "letra": "C", "texto": "$6{,}0 \times 10^{-4}\,\text{m}^2$" }
            ],
            "gabarito_adaptado": "B"
        },
        {
            "enunciado": """<p style="text-align:justify;"><b>(FAMEMA - 2021)</b> Um reservatório de água sem tampa apresentou uma trinca em seu fundo de tal forma que, para repará-lo, teve de ser esvaziado. Quando o reservatório foi novamente preenchido com água, observou-se que o tempo para o endurecimento do reparo não havia sido suficiente, pois, assim que o nível da água atingiu $2\,\text{m}$ em relação ao fundo, o reparo foi desfeito e a água começou a vazar. Sendo a pressão atmosférica igual a $1 \times 10^5\,\text{Pa}$, a aceleração da gravidade igual a $10\,\text{m/s}^2$, e a densidade da água igual a $1 \times 10^3\,\text{kg/m}^3$, <b>a pressão a partir da qual a água começou a vazar foi de</b></p>""",
            "tipo": "objetiva",
            "disciplina": "Física",
            "topico": "Mecânica",
            "conteudo": "Estática dos Fluidos",
            "assunto": "Teorema de Stevin",
            "banca": "FAMEMA",
            "ano": 2021,
            "dificuldade": "medio",
            "gabarito": "D",
            "alternativas": [
                { "letra": "A", "texto": "$1{,}0 \times 10^5\,\text{Pa}$." },
                { "letra": "B", "texto": "$0{,}2 \times 10^5\,\text{Pa}$." },
                { "letra": "C", "texto": "$0{,}4 \times 10^5\,\text{Pa}$." },
                { "letra": "D", "texto": "$1{,}2 \times 10^5\,\text{Pa}$." },
                { "letra": "E", "texto": "$1{,}5 \times 10^5\,\text{Pa}$." }
            ],
            "enunciado_adaptado": """<div style="text-align: justify;"><span style="font-size: 0.875rem;"><b>(FAMEMA - 2021)</b> Um reservatório de água tem uma trinca no fundo. O reparo cedeu e a água começou a vazar quando o nível da água atingiu $2\,\text{m}$ de profundidade. Sabe-se que a pressão atmosférica é $1 \times 10^5\,\text{Pa}$, a gravidade é $10\,\text{m/s}^2$ e a densidade da água é $1 \times 10^3\,\text{kg/m}^3$.</span></div><p><b>Qual foi a pressão total no fundo do reservatório no momento do vazamento?</b></p>""",
            "alternativas_adaptadas": [
                { "letra": "A", "texto": "$1{,}2 \times 10^5\,\text{Pa}$." },
                { "letra": "B", "texto": "$0{,}2 \times 10^5\,\text{Pa}$." },
                { "letra": "C", "texto": "$1{,}0 \times 10^5\,\text{Pa}$." }
            ],
            "gabarito_adaptado": "A"
        },
        {
            "enunciado": """<p style="text-align:justify;"><b>(UEA - 2023)</b> O Reservatório do Mocó foi criado para solucionar problemas no abastecimento de água na cidade de Manaus. Nele, dois imensos tanques feitos de ferro ficam elevados por uma imponente estrutura interna, também feita de ferro.</p><p style="text-align:center;">[IMAGEM]</p><p style="text-align:right;">Disponível em: https://www.guiamanaus.24h.blospot.com</p><p style="text-align:justify;">A elevação dos tanques garante a pressão necessária para a condução da água pelos encanamentos. Essa combinação de altura e pressão é utilizada em qualquer sistema de abastecimento, dos mais complexos aos mais simples, como no caso de caixas-d'água residenciais.</p><p style="text-align:justify;">Suponha que, no Reservatório do Mocó, exista uma tubulação vertical que mantém uma coluna de água com $4\,\text{m}$ de altura. Considerando a aceleração da gravidade igual a $10\,\text{m/s}^2$ e que a densidade da água seja $1 \times 10^3\,\text{kg/m}^3$, <b>a pressão hidrostática da água na base dessa coluna será</b></p>""",
            "tipo": "objetiva",
            "disciplina": "Física",
            "topico": "Mecânica",
            "conteudo": "Estática dos Fluidos",
            "assunto": "Pressão Hidrostática",
            "banca": "UEA",
            "ano": 2023,
            "dificuldade": "facil",
            "gabarito": "B",
            "alternativas": [
                { "letra": "A", "texto": "$20\,000\,\text{Pa}$." },
                { "letra": "B", "texto": "$40\,000\,\text{Pa}$." },
                { "letra": "C", "texto": "$50\,000\,\text{Pa}$." },
                { "letra": "D", "texto": "$60\,000\,\text{Pa}$." },
                { "letra": "E", "texto": "$80\,000\,\text{Pa}$." }
            ],
            "enunciado_adaptado": """<p style="text-align:center;">[IMAGEM]</p><p style="text-align:right;">Disponível em: https://www.guiamanaus.24h.blospot.com</p><div style="text-align: justify;"><span style="font-size: 0.875rem;"><b>(UEA - 2023)</b> A elevação dos reservatórios de água garante a pressão para a condução da água. Suponha que um tanque do Reservatório do Mocó mantenha uma coluna de água de $4\,\text{m}$ de altura. Considere a gravidade $10\,\text{m/s}^2$ e a densidade da água $1 \times 10^3\,\text{kg/m}^3$.</span></div><p><b>Qual será a pressão hidrostática da água na base dessa coluna?</b></p>""",
            "alternativas_adaptadas": [
                { "letra": "A", "texto": "$20\,000\,\text{Pa}$." },
                { "letra": "B", "texto": "$40\,000\,\text{Pa}$." },
                { "letra": "C", "texto": "$80\,000\,\text{Pa}$." }
            ],
            "gabarito_adaptado": "B"
        },
        {
            "enunciado": """<p style="text-align:justify;"><b>(FMJ - 2021)</b> Um submarino tripulado chinês chamado Fendouzhe (ou “lutador”, em português), chegou a um dos pontos mais profundos dos oceanos: a Fossa das Marianas, no Oceano Pacífico. O veículo fez 13 mergulhos entre outubro e novembro de 2020, e, em 8 deles, superou uma profundidade de 10 mil metros. O mais profundo foi em 10 de novembro de 2020, quando chegou a $10\,900\,\text{metros}$ abaixo da superfície.</p><p style="text-align:right;">Disponível em: https://olhardigital.com.br. (adaptado)</p><p style="text-align:justify;">Considere que a aceleração gravitacional seja igual a $10\,\text{m/s}^2$, que a densidade média da água do mar seja $1{,}03 \times 10^3\,\text{kg/m}^3$, e que a pressão interna do submarino seja igual à pressão atmosférica ao nível do mar. <b>Para atingir a profundidade máxima a que chegou, a estrutura do submarino deve suportar uma pressão de, no mínimo, aproximadamente,</b></p>""",
            "tipo": "objetiva",
            "disciplina": "Física",
            "topico": "Mecânica",
            "conteudo": "Estática dos Fluidos",
            "assunto": "Teorema de Stevin",
            "banca": "FMJ",
            "ano": 2021,
            "dificuldade": "medio",
            "gabarito": "C",
            "alternativas": [
                { "letra": "A", "texto": "$1{,}13 \times 10^{12}\,\text{Pa}$." },
                { "letra": "B", "texto": "$1{,}06 \times 10^{10}\,\text{Pa}$." },
                { "letra": "C", "texto": "$1{,}13 \times 10^8\,\text{Pa}$." },
                { "letra": "D", "texto": "$1{,}13 \times 10^7\,\text{Pa}$." },
                { "letra": "E", "texto": "$1{,}06 \times 10^{14}\,\text{Pa}$." }
            ],
            "enunciado_adaptado": """<p style="text-align:justify;">Um submarino tripulado chinês chegou a $10\,900\,\text{metros}$ de profundidade na Fossa das Marianas.</p><p style="text-align:right;">Disponível em: https://olhardigital.com.br. (adaptado)</p><div style="text-align: justify;"><span style="font-size: 0.875rem;"><b>(FMJ - 2021)</b> Na profundidade máxima, a aceleração gravitacional é $10\,\text{m/s}^2$, e a densidade da água do mar é $1{,}03 \times 10^3\,\text{kg/m}^3$. A pressão interna do submarino iguala a pressão atmosférica.</span></div><p><b>Qual pressão, no mínimo, a estrutura do submarino precisou suportar sob ataque da pressão externa?</b></p>""",
            "alternativas_adaptadas": [
                { "letra": "A", "texto": "$1{,}13 \times 10^7\,\text{Pa}$." },
                { "letra": "B", "texto": "$1{,}13 \times 10^8\,\text{Pa}$." },
                { "letra": "C", "texto": "$1{,}06 \times 10^{10}\,\text{Pa}$." }
            ],
            "gabarito_adaptado": "B"
        },
        {
            "enunciado": """<p style="text-align:justify;"><b>(PUC-RJ - 2021)</b> A pressão atmosférica na superfície de um lago é igual a $1{,}0 \times 10^5\,\text{Pa}$. Um mergulhador experimental mergulha nesse lago até uma profundidade tal que a pressão total sentida por ele é o triplo da pressão atmosférica externa. <b>Qual é a profundidade, em metros, em que se encontra o mergulhador?</b></p><p style="text-align:justify;"><b>Dados:</b> $g = 10\,\text{m/s}^2$; densidade da água $= 1{,}0\,\text{g/cm}^3$.</p>""",
            "tipo": "objetiva",
            "disciplina": "Física",
            "topico": "Mecânica",
            "conteudo": "Estática dos Fluidos",
            "assunto": "Teorema de Stevin",
            "banca": "PUC-RJ",
            "ano": 2021,
            "dificuldade": "medio",
            "gabarito": "A",
            "alternativas": [
                { "letra": "A", "texto": "20" },
                { "letra": "B", "texto": "15" },
                { "letra": "C", "texto": "10" },
                { "letra": "D", "texto": "5" },
                { "letra": "E", "texto": "0" }
            ],
            "enunciado_adaptado": """<div style="text-align: justify;"><span style="font-size: 0.875rem;"><b>(PUC-RJ - 2021)</b> A pressão atmosférica na superfície de um lago é de $1{,}0 \times 10^5\,\text{Pa}$. A pressão total sobre um mergulhador é o triplo desse valor. Considere gravidade $g = 10\,\text{m/s}^2$ e densidade da água $1{,}0\,\text{g/cm}^3$ ($1000\,\text{kg/m}^3$).</span></div><p><b>A que profundidade, em metros, está o mergulhador?</b></p>""",
            "alternativas_adaptadas": [
                { "letra": "A", "texto": "10 metros." },
                { "letra": "B", "texto": "20 metros." },
                { "letra": "C", "texto": "30 metros." }
            ],
            "gabarito_adaptado": "B"
        },
        {
            "enunciado": """<p style="text-align:justify;"><b>(PUC-RJ - 2021)</b> Dois garrafões idênticos são mantidos abertos à atmosfera e estão conectados por meio de um tubo muito fino. A válvula que os conecta encontra-se inicialmente fechada, como mostrado na figura. O garrafão da esquerda é preenchido com um óleo de densidade $0{,}8 \times 10^3\,\text{kg/m}^3$, e o da direita é preenchido com água, cuja densidade é $1{,}0 \times 10^3\,\text{kg/m}^3$, até que ambos tenham seus líquidos em uma altura de $1{,}0\,\text{metro}$ em relação ao fundo dos garrafões. A válvula, então, é aberta.</p><p style="text-align:justify;">[IMAGEM]</p><p style="text-align:justify;"><b>Após um tempo suficiente para que o sistema fique estático, qual é a altura final, em metros, da coluna de água à direita em relação ao fundo do garrafão?</b></p><p style="text-align:justify;"><b>Dado:</b> $g = 10\,\text{m/s}^2$.</p>""",
            "tipo": "objetiva",
            "disciplina": "Física",
            "topico": "Mecânica",
            "conteudo": "Estática dos Fluidos",
            "assunto": "Vasos Comunicantes",
            "banca": "PUC-RJ",
            "ano": 2021,
            "dificuldade": "dificil",
            "gabarito": "B",
            "alternativas": [
                { "letra": "A", "texto": "$0{,}8$" },
                { "letra": "B", "texto": "$0{,}9$" },
                { "letra": "C", "texto": "$1{,}0$" },
                { "letra": "D", "texto": "$1{,}2$" },
                { "letra": "E", "texto": "$1{,}8$" }
            ],
            "enunciado_adaptado": """<p style="text-align:justify;">Dois garrafões idênticos interligados iniciam com óleo e água separados por uma válvula.</p><p style="text-align:justify;">[IMAGEM]</p><div style="text-align: justify;"><span style="font-size: 0.875rem;"><b>(PUC-RJ - 2021)</b> A densidade do óleo é $0{,}8 \times 10^3\,\text{kg/m}^3$ e a da água é $1{,}0 \times 10^3\,\text{kg/m}^3$. Ambos tinham altura de $1{,}0\,\text{metro}$ antes da válvula abrir. A gravidade é $10\,\text{m/s}^2$.</span></div><p><b>Depois que a válvula abre e o sistema se estabiliza, qual é a nova altura em metros da coluna de água?</b></p>""",
            "alternativas_adaptadas": [
                { "letra": "A", "texto": "$0{,}9$" },
                { "letra": "B", "texto": "$0{,}8$" },
                { "letra": "C", "texto": "$1{,}0$" }
            ],
            "gabarito_adaptado": "A"
        },
        {
            "enunciado": """<p style="text-align:justify;"><b>(UEL - 2020)</b> A RioBotz, equipe de robótica da PUC-Rio, foi criada em 2003, quando estudantes, orientados pelo professor Marco Antônio Meggiolaro, decidiram construir robôs de combate. Hoje, a RioBotz é uma das 32 equipes que entraram na chave do Battlebots, programa de televisão norte-americano de luta de robôs. A equipe foi a única da América Latina a participar da competição.</p><p style="text-align:justify;">Suponha que o robô da RioBotz tenha massa de $18\,\text{kg}$ e possua uma lança cuja ponta apresenta uma área de secção transversal de $1\,\text{mm}^2$. Admita que a lança atinja uma parede perpendicularmente com velocidade de $15\,\text{m/s}$, recue com uma velocidade de $3\,\text{m/s}$, e que o período da colisão tenha durado $9\,\text{ms}$.</p><p style="text-align:justify;"><b>Com base nos conhecimentos de Física Mecânica, assinale a alternativa que apresenta corretamente a pressão (em Pa) exercida pela lança sobre a parede, desconsiderando atritos e deformações.</b></p>""",
            "tipo": "objetiva",
            "disciplina": "Física",
            "topico": "Mecânica",
            "conteudo": "Dinâmica",
            "assunto": "Impulso e Pressão",
            "banca": "UEL",
            "ano": 2020,
            "dificuldade": "dificil",
            "gabarito": "A",
            "alternativas": [
                { "letra": "A", "texto": "$3{,}6 \times 10^{10}$" },
                { "letra": "B", "texto": "$2{,}7 \times 10^9$" },
                { "letra": "C", "texto": "$5{,}4 \times 10^9$" },
                { "letra": "D", "texto": "$5{,}4 \times 10^{10}$" },
                { "letra": "E", "texto": "$3{,}6 \times 10^9$" }
            ],
            "enunciado_adaptado": """<p style="text-align:justify;">A equipe de robótica RioBotz desenvolveu um robô de combate de $18\,\text{kg}$. A lança do robô tem na ponta uma área de $1\,\text{mm}^2$.</p><div style="text-align: justify;"><span style="font-size: 0.875rem;"><b>(UEL - 2020)</b> A lança atinge uma parede a $15\,\text{m/s}$ e recua a $3\,\text{m/s}$ depois de uma colisão que durou $9\,\text{ms}$ ($9 \times 10^{-3}\,\text{s}$).</span></div><p><b>Qual foi a pressão em Pascal exercida pela lança sobre a parede durante a colisão?</b></p>""",
            "alternativas_adaptadas": [
                { "letra": "A", "texto": "$2{,}7 \times 10^9$" },
                { "letra": "B", "texto": "$3{,}6 \times 10^{10}$" },
                { "letra": "C", "texto": "$5{,}4 \times 10^9$" }
            ],
            "gabarito_adaptado": "B"
        },
        {
            "enunciado": """<p style="text-align:justify;"><b>(UFMS - 2022)</b> Um cuteleiro decidiu presentear seu melhor amigo, que é um grande admirador de ninjas e de samurais, com uma espada especial, jamais feita antes. Para confeccionar a espada, ele utilizou $210\,\text{gramas}$ de prata, cuja densidade é de aproximadamente $10{,}5\,\text{g/cm}^3$, $386\,\text{gramas}$ de ouro, cuja densidade é de aproximadamente $19{,}3\,\text{g/cm}^3$, e $1\,365\,\text{gramas}$ de um tipo especial de aço, cuja densidade é $7{,}8\,\text{g/cm}^3$. Ao final do processo de confecção, o cuteleiro percebeu que o volume da espada correspondia à soma dos volumes dos materiais utilizados. Para finalizar o processo de confecção, o artesão colocou a espada em uma caixa contendo um líquido cuja densidade é $3{,}04\,\text{g/cm}^3$. O que ocorreu na finalização da fabricação da espada? <b>Determine a resposta adequada quanto à densidade da espada e ao ocorrido quando esta foi colocada no referido líquido.</b></p>""",
            "tipo": "objetiva",
            "disciplina": "Física",
            "topico": "Mecânica",
            "conteudo": "Estática dos Fluidos",
            "assunto": "Impulsão e Densidade",
            "banca": "UFMS",
            "ano": 2022,
            "dificuldade": "medio",
            "gabarito": "C",
            "alternativas": [
                { "letra": "A", "texto": "A densidade da espada é $7{,}60\,\text{g/cm}^3$, e ela ficou totalmente imersa no líquido, pois é mais densa que o líquido." },
                { "letra": "B", "texto": "A densidade da espada é $7{,}60\,\text{g/cm}^3$, e ela flutuou no líquido, pois é mais densa que o líquido." },
                { "letra": "C", "texto": "A densidade da espada é $9{,}12\,\text{g/cm}^3$, e ela ficou totalmente imersa no líquido, pois sua densidade é o triplo da densidade do líquido." },
                { "letra": "D", "texto": "A densidade da espada é $9{,}12\,\text{g/cm}^3$, e ela flutuou no líquido, pois é menos densa que o líquido em três vezes." },
                { "letra": "E", "texto": "A densidade da espada é $37{,}6\,\text{g/cm}^3$, e ela afundou totalmente no líquido, pois é mais densa que o líquido." }
            ],
            "enunciado_adaptado": """<div style="text-align: justify;"><span style="font-size: 0.875rem;"><b>(UFMS - 2022)</b> Uma espada foi feita utilizando materiais com densidades diferentes. A densidade misturada (da espada como um todo) e seu comportamento em um líquido determinam o formato final. A densidade final da espada foi sendo avaliada contra a de um líquido de valor $3{,}04\,\text{g/cm}^3$.</span></div><p><b>Se a densidade calculada da espada for $9{,}12\,\text{g/cm}^3$, o que acontece com a espada quando jogada no líquido?</b></p>""",
            "alternativas_adaptadas": [
                { "letra": "A", "texto": "Afunda completamente, pois é três vezes mais densa que o líquido." },
                { "letra": "B", "texto": "Flutua na superfície, pois é menos densa que o líquido." },
                { "letra": "C", "texto": "Afunda completamente, pois a densidade da espada atinge $37{,}6\,\text{g/cm}^3$." }
            ],
            "gabarito_adaptado": "A"
        },
        {
            "enunciado": """<p style="text-align:justify;"><b>(ITA - 2020)</b> Considere um recipiente tubular fino, com área transversal constante, que contém dois líquidos imiscíveis A e B. As hastes verticais desse recipiente distam $20\,\text{cm}$ uma da outra ($L = 20\,\text{cm}$). Quando o recipiente está em repouso, o líquido A atinge uma altura de $80\,\text{cm}$ em relação à linha de separação dos líquidos. Quando o recipiente é colocado em movimento retilíneo uniformemente variado, a altura de A com relação à linha de separação dos líquidos passa a ser $H = 76\,\text{cm}$, conforme mostra a figura.</p><p style="text-align:justify;"><b>Dado:</b> $g = 10\,\text{m/s}^2$.</p><p style="text-align:center;">[IMAGEM]</p><p style="text-align:justify;"><b>Considerando-se que o sistema parte do repouso, a distância percorrida pelo recipiente após um intervalo de $3{,}0\,\text{s}$ é</b></p>""",
            "tipo": "objetiva",
            "disciplina": "Física",
            "topico": "Mecânica",
            "conteudo": "Estática dos Fluidos",
            "assunto": "Aceleração em fluidos",
            "banca": "ITA",
            "ano": 2020,
            "dificuldade": "dificil",
            "gabarito": "C",
            "alternativas": [
                { "letra": "A", "texto": "$2{,}4\,\text{m}$." },
                { "letra": "B", "texto": "$4{,}6\,\text{m}$." },
                { "letra": "C", "texto": "$9{,}0\,\text{m}$." },
                { "letra": "D", "texto": "$1{,}3 \times 10\,\text{m}$." },
                { "letra": "E", "texto": "$1{,}8 \times 10\,\text{m}$." }
            ],
            "enunciado_adaptado": """<div style="text-align: justify;"><span style="font-size: 0.875rem;"><b>(ITA - 2020)</b> Um recipiente tubular em forma de U suporta líquidos em movimento quando é acelerado. A mudança no nível entre as áreas do tubo depende dessa aceleração.</span></div><p style="text-align:center;">[IMAGEM]</p><p><b>Se sabemos que o sistema começou do repouso e estava sendo acelerado por $3{,}0\,\text{s}$, qual distância ele deve ter percorrido?</b></p>""",
            "alternativas_adaptadas": [
                { "letra": "A", "texto": "$4{,}6\,\text{m}$." },
                { "letra": "B", "texto": "$9{,}0\,\text{m}$." },
                { "letra": "C", "texto": "$1{,}8 \times 10\,\text{m}$." }
            ],
            "gabarito_adaptado": "B"
        }
    ]

    import os
    os.makedirs('saida', exist_ok=True)
    with open('saida/rascunho.json', 'w', encoding='utf-8') as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)

process_questions()
