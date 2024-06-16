# Nomes: Felipe Men dos Santos; Otho Oliveira Candido; Lucas Rodrigues de Queiroz; João Pedro Silva Pinheiro
# RMs: 557571; 55054; 556323; 557013

import time

# Mensagem de boas-vindas ao sistema
print("Seja Bem-Vindo(a) ao nosso sistema de estatísticas para os nossos pilotos!")
time.sleep(2)

# Lista para armazenar os dados dos pilotos
dados = []

# Função para criar uma nova lista (estatísticas do piloto)
def criar_lista():
    lista_nova = []
    return lista_nova

# Função para listar os dados dos pilotos
def listar_dados(dados):
    linhas = len(dados)
    colunas = 3
    print("Nome:    Melhor Volta:    Vitórias:")
    for i in range(linhas):
        for j in range(colunas):
            print(dados[i][j], end="     ")
        print()

# Função para remover um piloto da lista pelo índice
def remover_piloto(index):
    index -= 1  # Ajusta o índice para corresponder à posição na lista
    print(f"Piloto {dados[index][0]} removido com sucesso!")
    dados.pop(index)  # Remove o piloto da lista

# Função para obter as estatísticas de um novo piloto
def get_estatistica():
    while True:
        estatisticas = criar_lista()  # Cria uma nova lista para armazenar as estatísticas
        piloto = str(input("Digite o nome do piloto: "))
        if not piloto.isdigit():
            estatisticas.append(piloto)  # Adiciona o nome do piloto à lista
        else:
            print("Nome Inválido.")
            continue
        volta = str(input("Digite o tempo da melhor volta em segundos: "))
        if volta.isdigit():
            estatisticas.append(volta)  # Adiciona o tempo da melhor volta à lista
        else:
            print("Valor Inválido.")
            continue
        corrida = str(input("Digite a quantidade de corridas vencidas: "))
        if corrida.isdigit():
            estatisticas.append(corrida)  # Adiciona o número de corridas vencidas à lista
        else:
            print("Valor Inválido.")
            continue
        return estatisticas

# Função principal para o menu interativo
def main():
    while True:
        print("""
O que deseja fazer?
1 - Adicionar piloto
2 - Remover piloto
3 - Listar piloto(es)
4 - Sair
""")
        opcao = int(input("""

Escolha uma das opções: """))
        match opcao:
            case 4:
                # Encerra o programa
                print("Obrigado por utilizar nosso sistema!")
                break
            case 1:
                # Adiciona um novo piloto à lista de dados
                dados.append(get_estatistica())
            case 2:
                # Remove um piloto da lista de dados
                if not len(dados) == 0:
                    index = input("Digite o lugar/número do piloto que deseja remover: ")
                    if index.isdigit():
                        index = int(index)
                        remover_piloto(index)
                    else:
                        print("Valor Inválido")
                        continue
                else:
                    print("A lista de pilotos está vazia!")
            case 3:
                # Lista todos os pilotos e suas estatísticas
                if not len(dados) == 0:
                    listar_dados(dados)
                else:
                    print("A lista de pilotos está vazia!")
main()
