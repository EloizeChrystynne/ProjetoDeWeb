# 7. Atualizando
# Crie uma lista chamada estoque com valores numéricos representando a quantidade de cinco produtos. Peça
# ao usuário o índice (posição) de um produto e uma nova quantidade. Atualize o valor na lista e exiba o
# estoque atualizado.
# Exemplo de Saída:
# Estoque inicial: [10, 5, 8, 12, 4]
# Digite o índice do produto que deseja atualizar: 1
# Digite a nova quantidade: 9
# Estoque atualizado: [10, 9, 8, 12, 4]

estoque = [10, 9, 8, 2, 5]
posi = 0
qnt = 0
sn = "sim"

while sn == "sim":
  print("mudanca de estoque")
  print("na posição, digite de 0 a 4")
  print(estoque)
  posi = int(input("digite a posicao do produto que quer mudar: "))
  qnt = int(input("digite a nova quantidade do produto: "))
  estoque[posi] = qnt
  sn = input("de novo? (sim ou nao): ")
  
  
  if sn == "nao":
    print("estoque final abaixo")
    print (estoque)
    break