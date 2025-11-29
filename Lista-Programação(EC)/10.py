#Implemente um programa que simule um carrinho de compras. O programa deve:
#a. Criar uma lista vazia chamada carrinho;
#b. Pedir ao usuário que digite nomes de produtos para adicionar ao carrinho;
#c. Se o usuário digitar "remover", o programa deve pedir o nome de um produto e, se ele existir na lista,
#removê-lo;
#d. O programa encerra quando o usuário digita "sair";
#e. Ao final, exibe todos os produtos restantes no carrinho.

carrinho = []
loop = True

def menu():

    print("bem vindo ao menu de carrinho de compras:", carrinho)
    produto = input("digite o nome do produto para adicionar ao carrinho, 'remover' para retirar um produto ou 'sair' para encerrar: ")
    if len(carrinho) == 0:
        print("seu carrinho esta vazio")
    else:
        print("seu carrinho tem", carrinho, "produtos")
    return produto

def remover(produto):
    if produto in carrinho:
        carrinho.remove(produto)
    else:
        print("produto nao encontrado no carrinho")


while loop == True:
    produto = menu()
    if produto == "sair":
        print("carrinho final abaixo:")
        print(carrinho)
        print("obrigado por usar o sistema de carrinho de compras")
        loop = False
    elif produto == "remover":
        item = input("digite o nome do produto que deseja remover: ")
        remover(item)
    else:
        carrinho.append(produto)