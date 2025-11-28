#Crie uma lista chamada nomes com cinco nomes de colegas de turma. Peça ao usuário que digite um nome.
#Usando o for, verifique se o nome está na lista e exiba uma mensagem apropriada:,
#Nome encontrado na posição “X”!
#Nome não encontrado!

nomes = []
nome = 0
procurar = 0
achou = 0
loop = True
qnt = 0

while loop == True:
  print("nomes")
  nome = input("digite um nome: ")
  nomes.append(nome)             
  qnt = len(nomes)
  print(len(nomes))
  if qnt == 5:
    loop = False

procurar = input("digite o nome que deseja procurar: ") 

for i in range(len(nomes)):
  if nomes[i] == procurar:
    print(f"nome encontrado na posiçao {i}")
    achou = True

if not achou:
  print("nome nao encontrado")

