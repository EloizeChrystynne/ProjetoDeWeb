#Crie uma lista chamada tarefas.
#Peça ao usuário que digite tarefas até que ele digite "sair".
#Quando terminar, exiba:
#a) Quantas tarefas foram registradas
#b) Todas as tarefas, uma por linha
#Exemplo de Saída:
#Digite uma tarefa (ou 'sair' para encerrar): estudar
#Digite uma tarefa (ou 'sair' para encerrar): limpar o quarto
#Digite uma tarefa (ou 'sair' para encerrar): sair
#Você registrou 2 tarefas:
#- estudar
#- limpar o quarto

tarefas = []
tarefa = 0
qnt = 0
while True:
  tarefa = input("digite tarefas, digite 'sair' para parar: ")
  if tarefa == "sair":
    qnt = int(len(tarefas))
    print("voce registrou", qnt, "tarefas.")
    
    for i in range(len(tarefas)):
      print(i,"-",tarefas[i])
    break
  tarefas.append(tarefa)
  
  