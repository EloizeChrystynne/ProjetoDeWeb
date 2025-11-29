# Crie uma lista chamada assentos com os números de assentos disponíveis (por exemplo, [1, 2, 3, 4, 5, 6, 7, 8]).
# O programa deve:
# 1. Mostrar os assentos disponíveis;
# 2. Pedir ao usuário o número do assento que deseja reservar;
# 3. Verificar se o assento está livre:
#    - Se estiver, removê-lo da lista;
#    - Se não estiver, exibir mensagem de erro;
# 4. Repetir até que o usuário digite "fim".
# No final, exibir quantos assentos ainda estão disponíveis.

assentos = [1, 2, 3, 4, 5, 6, 7, 8]

loop =  True

def menu():
        print("bem vindo ao sistema de reservas de assentos")
        print("assentos disponiveis:", assentos)
        print("assentos reservados:", 8 - len(assentos))
        escolha = input("digite o numero do assento que deseja reservar ou digite fim para encerrar: ")
        return escolha

def reservar(escolha):
        numero = int(escolha)
        if numero in assentos:
                assentos.remove(numero)
        else:
                print("assento indisponivel, escolha outro assento")
        
while loop == True:
        escolha = menu()
        if len(assentos) == 0:
                print("infelizmente todos os assentos foram reservados")
                print("obrigado por ultilizar o sistema de reserva de assentos")
                break
        if escolha.isdigit():
                reservar(escolha)
        elif escolha == "fim":
                print("obrigado por ultilizar o sistema de reserva de assentos")
                loop = False
        else:
                print("entrada invalida, digite um numero ou fim")

