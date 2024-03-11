import os

produtos = ["Mousse", "Teclado", "Monitor"]

def criar_menu():
    os.system("cls")
    print("""

┏━━━┳┓╋╋╋╋┏━━━┓┏┓╋╋╋╋╋╋╋╋╋╋╋╋╋┏━━━┳━━━┳━━━┓
┃┏━┓┃┃╋╋╋╋┃┏━┓┣┛┗┓╋╋╋╋╋╋╋╋╋╋╋╋┃┏━┓┃┏━┓┃┏━┓┃
┃┃╋┗┫┗━┳━┳┫┗━━╋┓┏╋━━┳━━┳┓┏┳━━┓┃┃╋┃┃┗━┛┃┗━┛┃
┃┃╋┏┫┏┓┃┏╋╋━━┓┃┃┃┃┏┓┃┏┓┃┃┃┃┃━┫┃┗━┛┃┏━━┫┏━━┛
┃┗━┛┃┃┃┃┃┃┃┗━┛┃┃┗┫┗┛┃┗┛┃┗┛┃┃━┫┃┏━┓┃┃╋╋┃┃
┗━━━┻┛┗┻┛┗┻━━━┛┗━┻━━┻━┓┣━━┻━━┛┗┛╋┗┻┛╋╋┗┛
╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┃┃
╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┗┛""")
    print("Cadastro de Produtos\n")
    print("1. Cadastrar Produto")
    print("2. lista de Produtos")
    print("3. Ativar Produtos")
    print("4. Excluir Produto")
    print("5. Sair\n")

def voltar_ao_menu_principal():
    input("Pressione Enter para voltar ao menu principal...")
    main()
def criar_titulo(titulo):
    os.system("cls")
    print(f"***** {titulo} *****\n")

def cadastrar_produto():
    criar_titulo("Cadastro de Produtos")
    produto = input("Nome do Produto: ")
    produtos.append(produto)
    print(f"Produto {produto.upper()}, cadastrado com sucesso!\n")
    voltar_ao_menu_principal()

def mostrar_produtos():
    criar_titulo("Lista de Produtos")

    tamanho_vetor = len(produtos)

    print(f"Total de Produtos cadastrados: {tamanho_vetor}")
    for produto in produtos:
        print(produto)

    print()
    voltar_ao_menu_principal()


def tratar_erro():
    input("Valor Inválido! Pressione Enter para voltar ao menu principal...")
    main()


def escolher_opcao():

    try:
        opcao = int(input("\nEscolha uma opção (1 a 5): "))

        if opcao == 1:
            cadastrar_produto()

        elif opcao == 2:
            mostrar_produtos()

        elif opcao == 3:
            print("Você escolheu a opção 3")

        elif opcao == 4:
            print("Você escolheu a opção 4")

        elif opcao ==5:
           exit()

        else:
            tratar_erro()

    except:
        tratar_erro()




def main():
    criar_menu()
    escolher_opcao()

if __name__ == "__main__":
    main()
