#DICIONARIO DE USUARIOS.
logins = {
"jorbson"   : { "nome" :  "jorbson"   , "senha" : "#print" },
"neto"      : { "nome" :  "neto"      , "senha" : "nice"   },
"paulo"     : { "nome" :  "paulo"     , "senha" : "tobebo" },
"guilherme" : { "nome" :  "guilherme" , "senha" : "tampico"},
"eduardo"   : { "nome" :  "eduardo"   , "senha" : "drogas" },
"ricardo"   : { "nome" :  "ricardo"   , "senha" : "51pura" },
"adelson"   : { "nome" :  "adelson"   , "senha" : "0000"   },
"gabriel"   : { "nome" :  "gabriel"   , "senha" : "meve5"  },
}

#LOGIN VAI RECEBER O QUE FOR DIGITADO.
login = input('digite o login:')

#SENHA VAI RECEBER O QUE FOR DIGITADO.
senha = input('digite a senha:')

#VARIAVEL DEFINIDA COMO FALSA.
usuario_existe = False

#VERIFICANDO SE O LIGIN QUE FOI DIGITADO EXISTE NO DICIONARIO COMO USUARIO.
for usuario in logins:
    if login == usuario:
        usuario_existe = True
        break

if usuario_existe:
    usuario = logins[login]


    #VERIFICANDO SE A SENHA DO USUARIO ESTÁ CORRETA.
    if senha == usuario["senha"]:
        print ("bem vindo " + usuario["nome"])

    else:
        print("Senha invalida")
 
#USUARIO NÃO FOI ENCONTRADO NO DICIONARIO DE USUARIOS.
else:
    print("usuario" " " + login + " " "não está cadastrado")
