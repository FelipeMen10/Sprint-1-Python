#Nomes: Felipe Men dos Santos RMs: 557571

import time

print("Seja Bem-Vindo(a) ao nosso sistema de estatísticas para os nossos corredores!")
time.sleep(2)

dados = []

def criar_lista():
    lista_nova = []
    return lista_nova

def listar_dados(dados):
    linhas = len(dados)
    colunas = 3
    print("Nome:    Melhor Volta:    Vitórias:")
    for i in range(linhas):
        for j in range(colunas):
            print((i + 1), "-", dados[i][j], end="     ")
        print()
def remover_corredor(index):
    index -= 1
    dados.pop(index)
def get_estatistica():
    while True:
        estatisticas = criar_lista()
        corredor = str(input("Digite o nome do corredor: "))
        if not corredor.isdigit():
            estatisticas.append(corredor)
        else:
            print("Nome Inválido.")
            continue
        volta = str(input("Digite o tempo da melhor volta em segundos: "))
        if volta.isdigit():
            estatisticas.append(volta)
        else:
            print("Valor Inválido.")
            continue
        corrida = str(input("Digite a quantidade de corridas vencidas: "))
        if corrida.isdigit():
            estatisticas.append(corrida)
        else:
            print("Valor Inválido.")
            continue
        return estatisticas

def main():
    while True:
        print("""
O que deseja fazer?
1 - Adicionar corredor
2 - Remover corredor
3 - Listar corredor(es)
4 - Sair
""")
        opcao = int(input("""

Escolha uma das opções: """))
        match opcao:
            case 4:
                print("Obrigado por utilizar nosso sistema!")
                break
            case 1:
                dados.append(get_estatistica())
            case 2:
                if not len(dados) == 0:
                    index = input("Digite o lugar/número do corredor que deseja remover: ")
                    if index.isdigit():
                        index = int(index)
                        remover_corredor(index)
                        print("Corredor removido com sucesso!")
                    else:
                        print("Valor Inválido")
                        continue
                else:
                    print("A lista de corredores está vazia!")
            case 3:
                if not len(dados) == 0:
                    listar_dados(dados)
                else:
                    print("A lista de corredores está vazia!")
main()