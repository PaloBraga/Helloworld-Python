amigos= ["Felix", "Darlan", "Ricardo", "Adelson", "Guilherme"]

print(amigos[0])

print(amigos[1])

print(amigos[2])

print(amigos[3])

print(amigos[4])

print(amigos[-5])

print(amigos[-4])

print(amigos[-3])

print(amigos[-2])

print(amigos[-1])

#imprime um nome especifico da lisca

felix= amigos[0].title() + ", Cheguei e trouxe cerveja!"

darlan= amigos[1].title() + ", e ai mano, como tem passado?"

ricardo= amigos[2].title() + ", o departamento forte da EFO!"

adelson= amigos[3].title() + ", ei grande cade minha chave?"

guilherme= amigos[4].title() +", o mestre dos magos já sumiu..."

cap3= ", Cheguei e trouxe cerveja, cachaça e CARNE!"

print(felix)

print(darlan)

print(ricardo)

print(adelson)

print(guilherme)

print(amigos[0].title() + cap3)

carro=["\nVou comprar meu proximo carro!", "\nVou adquirir meu proximo carro, avista!", "\ncarro ou moto"]

print(carro[0].title())

print(carro[1].title())

print(carro[2].title())

motos=["honda", "yamaha", "kawasaki", "bmw"]

print(motos)

motos[0]="ducati"
#subistitui o nome da posição indicada na lista

print(motos)

motos[1]="suzuki"

print(motos)

motos[2]="kasisk"

print(motos)

motos[3]="sport"

print(motos)

motos.append("honda")
#adiciona um nome na lista, sem escolher posição.

print(motos)

motosvazias=[]

motosvazias.append("honda")
motosvazias.append("yamaha")

print(motosvazias)

motosvazias.append("kawasaki")

#adiciona um nome na lista, sem escolher posição

print(motosvazias)

motosvazias.insert(0,"BMW")

#adiciona um nome na lista, escolhendo a posição.

print(motosvazias)

motosvazias.insert(4, "sport")

#Escolhe a posição na lisca, onde será adicionado o nomme.

print(motosvazias)

del motosvazias[4]

#Deleta um nome da lista escolhendo a posição em que ele está.

print(motosvazias)

moto_removida_com_pop = motosvazias.pop(2)

print(motosvazias)

print(moto_removida_com_pop)

#Diferente da função "del" o ".pop", ele salva o item em um determinado campo.

print("Hoje em dia minha moto é uma "+ moto_removida_com_pop + "!")

motosvazias.remove("BMW")

print(motosvazias)

#PARA USAR A FUNÇÃO ".remove" VOCÊ PRECISA SABER O NOME DO ITEM QUE SERÁ EXCLUIDO.
motoexcluida="kawasaki"
motosvazias.remove(motoexcluida)

print(motosvazias)

print("A " + motoexcluida.title() + ", não esta mais na minha vontade de adquirir!")
print("")
#A FUNÇÃO ".REMOVE" TAMBÉM PODEMOS ARMAZENAR O ITEM PARA SER UTILIZADO FUTURAMENTE.

#PAG 81

cars=["bmw", "audi", "toyota", "subaru"]
cars.sort()
print(cars)
print("")

#FUNÇÃO COLOCA A LISTA EM ORDEM ALFABETICA

cars.sort(reverse=True)
print(cars)
print("")

#INFERNTE A ORDEM, COLOCANDO DE TRÁS PRA FRENTE

cars1=["honda","fiat", "vw", "bmw"]

print("A lista ordem é: ") 
print(sorted(cars1))
print("")
#MODO AUXILIAR DE COLOCAR A LISTA EM ORDEM, ESSE MODO TAMBÉ PODE SER ADICIONADO O "REVERSE=TRUE" PARA INVERTER A ORDEM ALFABÉTICA

print("A lista original é: ")
print(cars1)
print("")

#PAG 82 \/

cars1.reverse()
print(cars1)

cars1.reverse()
print(cars1)

print(len(cars1))

#FAÇA VOCÊ MESMO - PAG 83

localidades=["Serra do Mel","Natal","Macau","Rio de Janeiro"]

print(localidades)
print("")

print(sorted(localidades))
print("")

print(localidades)
print("")

localidades.sort(reverse=True)
print(localidades)
print("")

#Me confundi neste exercicio

#FAÇA VOCÊ MESMO PAG 84
cardapio=["sanduiche", "batata-frita", "cerveja"]
print(cardapio[2])
print("")

print(cardapio[-1])

#SE COLOCAR "print(cardapio[3])" DA O ERRO.

#FIM DO CAP 3