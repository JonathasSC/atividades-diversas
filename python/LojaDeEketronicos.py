def getMoneySpent(keyboards, drives, b):

    resposta = -1
    
    for k in keyboards:
        for d in drives:
            if k+d <= b and k+d > resposta:
                resposta = k+d
    
    return resposta

print(getMoneySpent([10,2,3],[3,1],8))

# Definindo resposta base caso o valor não seja encontrado: -1 

# para cada keyboard em keyboards faça outro loop para cada drive em drives:

# se a soma de keyboard e drive for menor ou igual ao orçamento ou maior que nossa resposta base:
# defina um novo valor para resposta 

# retorne resposta