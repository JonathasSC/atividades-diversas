def breakingRecords(scores):

	contador = menor = maior = pior_record = melhor_record = 0

	for score in scores: 
		if contador == 0:
			maior = menor = score
		else:
			if score > maior:
				maior = score
				melhor_record += 1
			if score < menor:
				menor = score
				pior_record += 1 
		contador += 1

	return melhor_record,pior_record	

breakingRecords([3, 4, 21, 36, 10, 28, 35, 5, 24, 42])