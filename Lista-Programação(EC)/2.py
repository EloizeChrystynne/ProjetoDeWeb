#Crie uma lista vazia chamada frutas. Peça ao usuário que digite o nome de várias frutas e adicione-as à lista
#com o método append(), até que ele digite “fim”. Depois, mostre todas as frutas cadastradas.
frutas = []
loop = True
fruta = 0

while loop == True:
  fruta = input("digite uma fruta, digite fim quando quiser parar: ")
  
  if fruta.lower() == "fim":
    print("essa é sua lista")
    print(frutas)
    loop = False
  if fruta.isdigit():
    print("nao digite numeros")
    continue
  if fruta.strip() == "":
    print("digite algo")
    continue
  frutas.append(fruta)
