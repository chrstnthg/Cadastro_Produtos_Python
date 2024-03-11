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
    print(produtos)
    print()
    voltar_ao_menu_principal()

def escolher_opcao():
    opcao = int(input("\nEscolha uma opção (1 a 5): "))

    if opcao == 1:
        cadastrar_produto()

    elif opcao == 2:
        mostrar_produtos()



def main():
    criar_menu()
    escolher_opcao()

if __name__ == "__main__":
    main()
