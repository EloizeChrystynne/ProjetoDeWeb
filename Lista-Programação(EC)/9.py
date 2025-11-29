#Em uma rede social escolar, o sistema precisa identificar palavras proibidas em mensagens dos usuários.
#Crie um programa que:
#a. Tenha uma lista chamada proibidas com palavras como ["violência", "ofensa", "ódio"];
#b. Peça ao usuário que digite uma mensagem;
#c. Use um for para verificar se a mensagem contém alguma das palavras proibidas (use o operador in);
#d. Mostre:
#○ "Mensagem aprovada" se estiver tudo certo;
#○ "Mensagem contém palavras proibidas!" Caso contrário.

proibidas = ["violência", "ofensa", "ódio"]
mensagem = input("digite sua mensagem: ")
proibido = False

for palavra in proibidas:
    print ("verificando...")
    if palavra in mensagem:
        proibido = True
        print("Mensagem contém palavras proibidas!")
        break
if proibido == False:
    print("Mensagem aprovada")
    print(mensagem)
