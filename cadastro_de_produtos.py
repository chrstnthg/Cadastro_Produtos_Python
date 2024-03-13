import os

produtos = [{
    "codigo": 100,
    "nome": "Mouse",
    "valor": 50.00,
    "fabricante": "Razer"

}, {
    "codigo": 200,
    "nome": "Teclado",
    "valor": 120.00,
    "fabricante": "Razer"

}, {
    "codigo": 300,
    "nome": "Monitor LED 17",
    "valor": 799.00,
    "fabricante": "Razer"

}]

produt44s = ["Mouse", "Teclado", "Monitor"]

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
        print("Codigo                         Nome                          Valor")
        codigo = produto["codigo"]
        nome = produto["nome"]
        valor = produto["valor"]
        fabricante = produto["fabricante"]

        print(f"{codigo:<30} {nome:<30}  R${valor:>6}  {fabricante:<30}")

    print()
    voltar_ao_menu_principal()


def tratar_erro():
    input("Valor Inválido! Pressione Enter para voltar ao menu principal...")
    main()

def tratar_erro_produto():
    input("Valor Inválido! Pressione Enter e tente novamente...")
    excluir_produto()

def excluir_produto():
    criar_titulo("Excluir Produto")

    indice = int(input("Qual produto que será removido? "))
    confirmacao = input(f"Você confirmação a exclusão do produto {produtos[indice]}(s/n)? ")

    try:
        if confirmacao == "s":
            excluido = produtos.pop(indice)
            print(f"O produto {excluido} foi excluido com sucesso!")
            voltar_ao_menu_principal()
        elif confirmacao == "n":
            print("Operação de exclusão cancelada")
            voltar_ao_menu_principal()
        else:
            tratar_erro_produto()
    except:
        tratar_erro_produto()
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
           excluir_produto()

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
