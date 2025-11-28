#Crie uma lista chamada materias com as disciplinas do curso técnico. Peça ao usuário o nome de uma
#matéria e, se ela estiver na lista, remova-a. Imprima a lista atualizada.
materia = ["infobasica", "introducaoaprogramacao", "arquitetura"]
loop = True
remover = 0


while loop == True:
  print(materia)
  remover = input("digite uma disciplina para remover: ")
  if remover in materia:
    materia.remove(remover)
    continue
  if len(materia) ==0:
    print("nao há mais nada pra remover")
    break
