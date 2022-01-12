magicos=["Paulo", "Nemezio", "Felix"]

for magico in magicos:


    print(magico.title()+", isso é um otimo truque!")
print("")

# ESSE LIVRO QUE ME ENDOIDA, DEU ERRO, ERRO, AÍ COM UM "TAB" ANTES NO PRINT, TUDO FOI RESOLVIDO(ISSO O LIVRO NÃO DIZ).

gatos=["pantera", "Lok", "feifei"]

for gato in gatos:
    print(gato.title()+", você só dorme?")
print("")

cachorros=["thor", "teo", "biscoito"]

for cachorro in cachorros:
    print(cachorro.title()+ ", hoje é dia de lata!")    
print("")

ferramentas=["alicate", "chave filips", "multimetro"]

for ferramenta in ferramentas:
    print(ferramenta.title())
print("")

#PAG 89

magicos=["Paulo", "Nemezio", "Felix"]

for magico in magicos:


    print("Estamos ansioso para o proximo truque, "+ magico.title()+"!\n")
    print(magico.title()+", isso é um otimo truque!\n")

#PAG 90
for magico in magicos:
    print(magico.title()+ ", foi um ótimo truque! \n")
    print("Mal posso esperar para ver seu próximo truque, "+ magico.title()+ "!\n")

#PAG 94 - EXERCICIO

pizzas=["calabresa", "frango", "carne de sol"]

for pizza in pizzas:
    print(pizza)
    print("")

for adoro in pizzas:
    print("Eu adoro pizza de " +adoro.title())
    print("")

animais=["cão", "gato", "rato"]

for animal in animais:
    print("Um "+ animal +", é um otimo animal!")

#PAG 95

for valor in range(1,5):
    print(valor)
print("")
#ESTE COMANDO IMPRIME OS NÚMEROS DO 1 AO 4, CASO QUEIRA IMPRIMIR OS 5 OU MAIS, COLOCAR SEMPRE UM NÚMERO A MAIS.
for valor in range(1,6):
    print(valor)
print("")
#AGORA APÓS ADICIONAR UM NÚMERO A MAIS ELE IMPRIMI DO 1 AO 5.

#PAG 96

numero= list(range(1,6))
print(numero)
print("")

#O PROXIMO CÓDIGO PERMITE QUE O PYTHON SOME OS NUMEROS ATÉ O NÚMERO PRE-DETERMINADO.
#SOMA SEMPRE +2
numero2= list(range(2,11,2))
print(numero2)
print("")
#SOMA SEMPRE +4
numero2= list(range(2,11,4))
print(numero2)
print("")

squares=[]
for valor in range(1,22):
    squares.append(valor**2)
    print(squares)
print("")

#PAG 97

digitos=[1,2,3,4,5,6,7,8,9,0]
min(digitos)
max(digitos)
sum(digitos)

print(digitos) 

#FAÇA VOCÊ MESMO PAG 98

