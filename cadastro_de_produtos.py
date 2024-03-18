import os

produtos = [{
    "codigo": 100,
    "nome": "Mouse",
    "valor": 50.00,
    "fabricante": "Razer",
    "status": "ativo"
}, {
    "codigo": 200,
    "nome": "Teclado",
    "valor": 120.00,
    "fabricante": "Razer",
    "status": "ativo"

}, {
    "codigo": 300,
    "nome": "Monitor LED 17",
    "valor": 799.00,
    "fabricante": "Razer",
    "status": "ativo"

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

    codigo = input("Codigo do produto: ")
    nome = input("Nome do Produto: ")
    valor = float(input("Valor do Produto: "))
    fabricante = input("Fabricante do Produto: ")

    produtos.append(
        {
            "codigo": codigo,
            "nome": nome,
            "valor": valor,
            "fabricante": fabricante,
            "status": True
        }
    )
    print(f"Produto {nome.upper()}, cadastrado com sucesso!\n")
    voltar_ao_menu_principal()

def alterar_status_produto():
    criar_titulo("Alterar Status do Produto")
    codigo_produto = input("Digite o código do produto que deseja alterar: ")
    produto_encontrado = False
    for produto in produtos:
        if produto["codigo"] == codigo_produto:
            produto_encontrado = True
            novo_status = input("Digite 'ativar' para ativar ou 'desativar' para desativar o produto: ").lower()
            if novo_status == "ativar":
                produto["ativo"] = True
                print("Produto ativado com sucesso!")
            elif novo_status == "desativar":
                produto["inativo"] = False
                print("Produto desativado com sucesso!")
            else:
                print("Entrada inválida! Por favor, digite 'ativar' ou 'desativar'.")

    if not produto_encontrado:
        print("Produto não encontrado!")
    voltar_ao_menu_principal()

def mostrar_produtos():
    criar_titulo("Lista de Produtos")

    tamanho_vetor = len(produtos)
    total_produtos_ativos = 0

    print("Codigo                         Nome                          Valor")
    for produto in produtos:
        if produto["ativo"]:
            codigo = produto["codigo"]
            nome = produto["nome"]
            valor = produto["valor"]
            fabricante = produto["fabricante"]
            print(f"{codigo:<30} {nome:<30}  R$ {valor:>6}  {fabricante:<30}")
            total_produtos_ativos += 1

    print(f"Total de Produtos cadastrados: {total_produtos_ativos}")
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
            alterar_status_produto()

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
