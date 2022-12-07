def GetTotalX(a, b): 
	counter = 0 #Contador 
	for indice in range(max(a), min(b)+1): # para cada indice no raio de ( maximo da lista 1 e minimo da lista 2 + 1)
		fator = True # Fator inicial = VErdadeiro
		for Avalues in a: # Para cada Valor A na lista A:
			if indice % Avalues != 0: # Se o resto da divisão de indice e Valor A for diferente de 0: 
				fator = False # Valor do fator torna-se Falso
				break # Pare.
		for Bvalues in b: # Para cada Valor B na lista B:
			if Bvalues % indice != 0: # Se o resto da divisão de Valor B e o indice for diferente de 0:
				fator = False # fator torna-se Falso
				break # Pare
		if fator == True: # Se o fator for Verdadeiros, some 1 ao contador.
			counter += 1
	return counter
GetTotalX([2,6],[24,36])