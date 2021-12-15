listadeconvidados=["Ant-Cristo", "Mestre dos Magos", "Cachaceiro Raiz"]
#Manda eu adicionar
naovai="Mestre dos Magos"
#MANDA EU TIRAR
listadeconvidados.remove(naovai)
print("O "+naovai + ", não ira comparecer!")
#FAZER UMA MENSAGEM PARA TIRAR UM CONVIDADO
listadeconvidados.insert(1,"Aliciador de Novinhas")
#ADD UM CONVIDADO NO LUGAR DO QUE SAIU
listadeconvidados.insert(3, "Erismar")
listadeconvidados.insert(4, "Ricardo")
listadeconvidados.insert(5, "Nemezio")
#ADICIONAR MAIS 3 CONVIDADOS
adelson=listadeconvidados.pop(1)
print("O livro galado mandou eu cancelar, "+ adelson.title())
erismar=listadeconvidados.pop(2)
print("O livro galado mandou eu cancelar, "+ erismar.title())
ricardo=listadeconvidados.pop(2)
print("O livro galado mandou eu cancelar, "+ ricardo.title())
nemezio=listadeconvidados.pop(2)
print("O livro galado mandou eu cancelar, "+ nemezio.title())
#AGORA O BAITOLA, MANDA EU CANCELAR COM 4 CONVIDADOS
print("")
print(listadeconvidados)
print("Ainda está confirmado," + listadeconvidados[0].title() +"!")
print("")
print("Ainda está confirmado," + listadeconvidados[1].title() +"!")
print("")
#MENSAGEM PARA OS 2 QUE AINDA ESTÃO CONVIDADOS
del listadeconvidados[0]
del listadeconvidados[0]
#AGORA MANDOU DELETAR TODOS OS CONVIDADOS
print(listadeconvidados)
#ASSIM A LISTA ESTA VAZIA
print("")
