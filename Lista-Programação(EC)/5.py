#crie uma lista chamada notas. Peça ao usuário que digite várias notas (valores numéricos) e adicione-as à
#lista. O programa vai aceitar notas até que seja digitado -1. Depois, calcule e exiba:
#a) A média das notas
#b) A maior e a menor nota
import math

notas = []
while True:
  valor = int(input("digite varias notas, digite -1 para parar: "))
  if valor == -1:
    print (notas)
    break
  notas.append(valor)
  
if len(notas) > 0:
  media = sum(notas)/len(notas)
  maior = max(notas)
  menor = min(notas)
    
  print("Resultado", media)
  print ("o maior numero é", maior)
  print ("o menor numero é", menor)
else:
  print("nenhuma nota foi digitada")
    
  

    


  