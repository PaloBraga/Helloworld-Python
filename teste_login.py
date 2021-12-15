logins = {
"jorbson": { "nome" : "jorbson" , "senha" : "1234" },
"neto"   : { "nome" :  "neto"   , "senha" : "2345" },
"paulo"  : { "nome" :  "paulo"  , "senha" : "3456" },
}

login = input('digite o login:')

senha = input('digite a senha:')

usuario_existe = False

for usuario in logins:
    if login == usuario:
        usuario_existe = True
        break

if usuario_existe:
    usuario = logins[login]


    #if senha == logins[login]["senha"]:
    if senha == usuario["senha"]:
        print ("bem vindo " + usuario["nome"])

    else:
        print("Senha invalida")
 
else:
    print("usuario não existe " + login)
    