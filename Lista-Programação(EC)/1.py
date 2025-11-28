#Crie uma lista chamada produtos com cinco nomes de produtos de supermercado. Imprima:
#a) Usando um laço while, exiba cada produto na tela, um por linha.
#b) Quantos produtos estão cadastrados;
#c) O primeiro e o último produto da lista;

produtos = ["coca", "pepsi", "fanta", "sprite", "guarana", "fantauva"]
indice = 0
qnt = len(produtos)

while indice < len(produtos):
  print("produto:", produtos[indice])
  indice += 1
print("Quantidade de produtos:", qnt)

print("o ultimo item é:", produtos[qnt-1] )
print("o primeiro item é:", produtos[0] )