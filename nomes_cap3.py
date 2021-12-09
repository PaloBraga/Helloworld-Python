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

