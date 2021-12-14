
# ESSE ARQUIVO EXECUTA UMA ROTINA PARA ESCOLHER UM DRINK
# DE ACORDO COM A OPÇÃO INFORMADA NO CARDAPIO


# O ELEMENTO "cardapio" É UM DICIONARIO, DEFINIDO PELAS CHAVES {}
# E ELE RECEBE UMA OU VARIOS ELEMENTOS NO FORMATO {"CHAVE" : "VALOR" ,"CHAVE" : "VALOR" , "CHAVE" : "VALOR" , n}
# ONDE, AO CHAMAR A CHAVE, ELE RETORNARA O VALOR ATRIBUIDO A ELA

cardapio = {
    # chave : valor
    "1" : "cana",
    "2" : "cerveja",
    "3" : "conhaque",
}


# CHAMANDO O CONTEUDO COMPLETO DO CARDAPIO EM UM PRINT
# VAI MOSTRAT TODA SUA ESTRUTURA, INCLUINDO CHAVES E VALORES

print("O cardpio tem:")
print(cardapio)

# PARA ESCOLHER UM VALOR ESPECIFICO DE UMA DAS CHAVES, UTILIZAMOS O COLCHETES [] COMO SELETOR E PASSAMOS A CHAVE PARA BUSCA
# NO FORMATO DICIONARIO[CHAVE]  Ex.: cardapio["1"], deve retornar > "cana"

print("Felix vai beber:")
print(cardapio["1"])
print("")

print("Paulo vai beber :")
print(cardapio["2"])
print("")

print("Jorbson vai beber :")
print(cardapio["3"])
print("")

print("Eazy and Nice ;)")