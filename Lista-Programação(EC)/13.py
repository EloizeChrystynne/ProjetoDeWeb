# Último chefe – Jogo da Adivinhação de Palavras
# Você vai criar um jogo de adivinhação estilo "Forca", usando listas para controlar o progresso do jogador.
# O programa deve:
# 1. Definir uma palavra secreta (exemplo: "python").
# 2. Criar uma lista chamada letras_descobertas que inicialmente contém apenas _ (um sublinhado para
#    cada letra da palavra).
# 3. Pedir ao jogador que digite uma letra por vez.
# 4. A cada tentativa:
#    - Se a letra estiver na palavra, revelar todas as ocorrências dela na lista letras_descobertas.
#    - Se não estiver, exibir uma mensagem de erro e contar uma tentativa incorreta.
# 5. O jogo termina quando o jogador descobre toda a palavra ou atinge 6 erros.
# 6. Ao final, o programa deve exibir se o jogador venceu ou perdeu, e mostrar a palavra completa.

palavra = "brasil"
letras_descobertas = ["_"] * len(palavra)
erros = 0
loop = True

while loop == True:

    print(letras_descobertas)
    letra = input("digite uma letra: ")

    if letra in palavra:
        indice = 0
        while indice < len(palavra):
            if palavra[indice] == letra:
                letras_descobertas[indice] = letra
            indice += 1
    else:
        print("letra errada")
        erros += 1
        print("erros:", erros)

    
    if "_" not in letras_descobertas:
        print("voce venceu")
        print("a palavra era:", palavra)
        loop = False


    if erros == 6:
        print("voce perdeu")
        print("a palavra era:", palavra)
        loop = False

