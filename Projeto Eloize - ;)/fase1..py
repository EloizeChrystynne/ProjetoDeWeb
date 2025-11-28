filmes = []


def carregar():
    try:
        arquivo = open("filmes.txt", "r", encoding="utf-8")
        for linha in arquivo:
            linha = linha.strip()       
            nome, diretor = linha.split(";")
            filmes.append([nome, diretor])
        arquivo.close()
    except FileNotFoundError:
        pass   


def salvar():
    arquivo = open("filmes.txt", "w", encoding="utf-8")
    for filme in filmes:
        arquivo.write(f"{filme[0]};{filme[1]}\n")
    arquivo.close()

def cadastrar():
    nome = input("Nome do filme: ")
    diretor = input("Diretor do filme: ")
    filmes.append([nome, diretor])
    print("Filme cadastrado!")

def listar():
    if len(filmes) == 0:
        print("Nenhum filme cadastrado.")
    else:
        for i in range(len(filmes)):
            print(i, "-", filmes[i][0], "(Diretor:", filmes[i][1] + ")")

def remover():
    listar()
    if len(filmes) == 0:
        return
    indice = int(input("Número do filme que deseja remover: "))
    filmes.pop(indice)
    print("Filme removido.")

def pesquisar():
    nome_busca = input("Nome para buscar: ")
    encontrado = False
    for filme in filmes:
        if nome_busca.lower() in filme[0].lower():
            print(filme[0], "(Diretor:", filme[1] + ")")
            encontrado = True

    if not encontrado:
        print("Nenhum filme encontrado.")

def menu():
    carregar()   
    while True:
        print("""
1 - Cadastrar filme
2 - Listar filmes
3 - Remover filme
4 - Pesquisar filme
5 - Sair
        """)

        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            remover()
        elif opcao == "4":
            pesquisar()
        elif opcao == "5":
            salvar()   
            print("Saindo... Dados salvos!")
            break
        else:
            print("Opção inválida!")

menu()
