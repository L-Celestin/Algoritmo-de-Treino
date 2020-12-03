#Banco de dados dentro do proprio código
musculos = [
    'CBT', 'COSTAS', 'COSTA', 'BÍSCEPS', 'BISCEPS', 'TRAPÉZIO', 'PERNAS',
    'PERNA', 'TRÍSCEPS', 'TRISCEPS'
]

CBTL = ["CBT", "COSTAS", "BÍSCEPS", "BISCEPS", "TRAPÉZIO", "COSTA", 'TRAPEZIO']
PERL = ["PERNAS", "PERNA"]
TRISL = ["TRÍSCEPS", "TRISCEPS"]

cbt = {
    1: ({
        'APARELHO': 'PUXADOR 1',
        'LOCALIZAÇÃO': 'E04',
        'INSTRUÇÕES': ''
    }),
    2: ({
        'APARELHO': 'PUXADOR 2',
        'LOCALIZAÇÃO': 'E05',
        'INSTRUÇÕES': ''
    }),
    3: ({
        'APARELHO': 'GRAVITATION',
        'LOCALIZAÇÃO': 'E04',
        'INSTRUÇÕES': ''
    }),
    4: ({
        'APARELHO': 'REMADA CAVADA',
        'LOCALIZAÇÃO': 'D11',
        'INSTRUÇÕES': ''
    }),
    5: ({
        'APARELHO': 'ROSCA BARRA W (BÍCEPS)',
        'LOCALIZAÇÃO': 'E07',
        'INSTRUÇÕES': ''
    }),
    6: ({
        'APARELHO': 'TRAPÉZIO COM BARRA',
        'LOCALIZAÇÃO': 'E07',
        'INSTRUÇÕES': ''
    }),
    7: ({
        'APARELHO': 'ROSCA DE BÍSCEPS COM ALTERES ALTERNADOS',
        'LOCALIZAÇÃO': '',
        'INSTRUÇÕES': ''
    })
}

pernas = {
    1: ({
        'APARELHO': 'EXTENSORA',
        'LOCALIZAÇÃO': 'D02',
        'INSTRUÇÕES': ''
    }),
    2: ({
        'APARELHO': 'FLEXORA DEITADO',
        'LOCALIZAÇÃO': 'D03',
        'INSTRUÇÕES': ''
    }),
    3: ({
        'APARELHO': 'ABDUÇÃO',
        'LOCALIZAÇÃO': '',
        'INSTRUÇÕES': ''
    }),
    4: ({
        'APARELHO': 'LEG VERTICAL',
        'LOCALIZAÇÃO': 'D07',
        'INSTRUÇÕES': ''
    }),
    5: ({
        'APARELHO': 'LEG 45',
        'LOCALIZAÇÃO': 'D08',
        'INSTRUÇÕES': ''
    }),
    6: ({
        'APARELHO': 'HACK',
        'LOCALIZAÇÃO': 'D09',
        'INSTRUÇÕES': ''
    }),
    7: ({
        'APARELHO': 'PANTURRILHA',
        'LOCALIZAÇÃO': '',
        'INSTRUÇÕES': ''
    })
}

trisceps = {
    1: {
        'APARELHO': 'SUPINO REGULÁVEL',
        'LOCALIZAÇÃO': 'D06',
        'INSTRUÇÕES': ''
    },
    2: {
        'APARELHO': 'BANCO SUPINO',
        'LOCALIZAÇÃO': 'D11',
        'INSTRUÇÕES': ''
    },
    3: {
        'APARELHO': 'BANCO SUPINO INCLINADO',
        'LOCALIZAÇÃO': 'E09',
        'INSTRUÇÕES': ''
    },
    4: {
        'APARELHO': 'SUPINO VERTICAL',
        'LOCALIZAÇÃO': 'D14',
        'INSTRUÇÕES': ''
    },
    5: {
        'APARELHO': 'DESENVOLVIMENTO ARTICULADO',
        'LOCALIZAÇÃO': 'D13',
        'INSTRUÇÕES': ''
    },
    6: {
        'APARELHO': 'ELEVAÇÃO LATERAL',
        'LOCALIZAÇÃO': '',
        'INSTRUÇÕES': ''
    },
    7: {
        'APARELHO': 'TRÍSCEPS FRANCÊS',
        'LOCALIZAÇÃO': 'D01',
        'INSTRUÇÕES': ''
    },
    8: {
        'APARELHO': 'TRÍSCEPS NA CORDA',
        'LOCALIZAÇÃO': 'D01',
        'INSTRUÇÕES': ''
    }
}


#Definição das funções que auxiliaram o algorítmo.
def borda():
    print()
    print("}----------/ ----------/ ----------/ ----------/ ----------{")
    print()


def adicionar(lista_exercícios):
    nome = input("Qual é o nome do aparelho?: ").strip().upper()
    loc = input("Localização do aparelho: ").strip().upper()
    info = input("Informações para Realizações do Treino: ").strip().lower()
    t = {'APARELHO': nome, 'LOCALIZAÇÃO': loc, 'INSTRUÇÕES': info}
    n = len(lista_exercícios) + 1
    lista_exercícios[n] = t
    print()
    print(
        "Aqui está sua lista até agora, por favor adicione ela ao algoritmo.")
    print(lista_exercícios)


def treinos(lista_exercícios):
    print("Quantos treinos vai realizar hoje?")
    print()
    print("(1) Quantidade padrão (7 treinos)")
    print("(2) Escolher quantidade.")
    print()
    c2 = int(input("Escolha uma das opções acima: "))
    if c2 == 1:
        i = 8
        ni = 0
        while i != 0:
            ni = ni + 1
            i = i - 1
            print(lista_exercícios.get(ni))
    if c2 == 2:
        ni = 1
        i = int(input("Quantos treinos vai realizar?: ")) + 1
        while i != 0:
            ni = ni + 1
            i = i - 1
            print(lista_exercícios.get(ni))


#Código
n = 0
while n != 3:
    borda()
    print("(1) Adicionar treino.")
    print("(2) Gerar treino.")
    print("(3) sair.")
    print()
    n = int(input("Selecione uma opção: "))
    if n == 1:
        borda()
        m = input("Para qual parte do corpo é o treino?: ").strip().upper()
        if m in musculos:
            print()
            print(
                "< obs: se não quiser adicionar informações apenas aperte enter. >"
            )
            print()
            if m in CBTL:
                adicionar(cbt)
            if m in PERL:
                adicionar(pernas)
            if m in TRISL:
                adicionar(trisceps)
        else:
            print()
            print(
                "< Não encontramos esse músculo, por favor adicione ao algorítmo. >"
            )
    if n == 2:
        borda()
        print("(1) Gerar treino qualquer.")
        print("(2) Gerar treino recomendado (dias da semana)")
        c1 = int(input("Escolha uma das opções acima: "))
        if c1 == 1:
            borda()
            musc = input("Qual o músculo vai treinar hoje?: ").strip().upper()
            if musc in musculos:
                if musc in CBTL:
                    borda()
                    treinos(cbt)
                if musc in PERL:
                    borda()
                    treinos(pernas)
                if musc in TRISL:
                    borda()
                    treinos(trisceps)
        if c1 == 2:
            dia_da_semana = input("Para qual dia da semana?: ")
            print()
    if n == 3:
        borda()
        print("Programa Finalizado.")
