#Crie um programa que simule o cadastro de usuários em um site. O programa deve:
#1. Criar duas listas vazias:
#usuarios → para armazenar os nomes dos usuários
#emails → para armazenar os respectivos e-mails
#2. Pedir ao usuário que digite o nome e o e-mail (ou "sair" para encerrar).
#3. Não permitir o cadastro de nomes repetidos (verifique se o nome já existe na lista).
#4. Ao final, exibir:
#○ A lista completa de usuários e e-mails (lado a lado);
#○ O total de cadastros;
#○ E permitir que o usuário digite um nome para pesquisar seu e-mail

usuarios = []
emails = []
loop = True
nome = 0

def menu():
    nome = input("digite o nome do usuario para cadastrar ou 'sair' para encerrar: ")
    return nome

def cadastrar():
    email = input("digite o email do usuario: ")
    usuarios.append(nome)
    emails.append(email)


def procurar():
    busca = input("digite o nome do usuario que deseja buscar o email: ")
    if busca in usuarios:
        indice = usuarios.index(busca)
        print("o email do usuario", busca, "é:", emails[indice])
    else:
        print("usuario nao encontrado")

while loop == True:
    nome = menu()
    if nome == "sair":
        print("lista de usuarios e emails cadastrados:")
        for i in range(len(usuarios)):
            print("usuario:", usuarios[i], "| email:", emails[i])
        print("total de cadastros:", len(usuarios))
        procurar()
    
        loop = False
    elif nome in usuarios:
        print("usuario ja cadastrado, tente outro nome")
    else:
        cadastrar()

