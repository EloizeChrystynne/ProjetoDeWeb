# Crie uma lista vazia chamada mochila = [].
# Mostre o seguinte menu em um laço while:
# === Mochila do Aventureiro ===
# 1 - Adicionar item
# 2 - Remover item
# 3 - Mostrar mochila
# 4 - Sair
# Escolha uma opção:
# Regras do jogo:
# A mochila tem espaço máximo para 5 itens.
# Só é possível adicionar itens enquanto não estiver cheia.
# O jogador pode remover um item digitando o nome.
# Quando ele escolher sair, o jogo mostra:
# - Todos os itens na mochila.
# - Se o jogador conseguir pegar os 3 itens essenciais: "mapa", "lanterna" e "corda".
# Se sim → mensagem: "Você está pronto para a aventura!"
# Caso contrário → "Você esqueceu algo importante!"

mochila = []
essencia = ["mapa", "lanterna", "corda"]
loop = True

def menu():
    print("=== Mochila do Aventureiro ===")
    print("1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Mostrar mochila")
    print("4 - Sair")
    escolha = int(input("Escolha uma opção: "))
    return escolha


def adicionar():
    item = input("escolha um item para adicionar: ")
    mochila.append(item)

def remover():
    item2 = input("escolha um item pra remover: ")
    mochila.remove(item2)

def mostrar():
    print(mochila)


while loop == True:
    escolha = menu()
    if escolha == 1:
        adicionar()
        if len(mochila) == 6:
            mochila.pop(5)
            print("ultimo item removido")
            print("mochila cheia")
    if escolha == 2:
        remover()
    if escolha ==3:
        mostrar()
    if escolha == 4:
        print("voce levou estes itens:")
        print(mochila)
        if all(item in mochila for item in essencia):
            print("voce esta pronto para aventura")
        else:
            print("voce esqueceu algo importante")
        break
    if len(mochila) == 6:
        mochila.pop(5)
        print("mochila cheia")


        


#if escolha == 4:
        #print("voce levou estes itens:")
        #print(mochila)
        #if essencia in mochila:
        #    print("voce esta pronto para aventura")
        #else:
        #    print("voce esqueceu algo importante")

#codigo anterior, que nao funcionou, devido a isso pesquisei e descobri a funçao all() que me permitiu resolver o problema, pois nao teria como fazer isso sem ela, a nao ser que eu usasse
#um contador com for, pra cada item em essencia e mochila individualmente. mas com a funcao all fica mais curto.
#if len(mochila) <= 5: