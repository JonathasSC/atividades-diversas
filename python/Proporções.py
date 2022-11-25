def plusMinus(arr):
    n = len(arr)
    positivos = []
    negativos = []
    zeros = []

    for element in range(n):
        if arr[element] > 0 :
            positivos.append(arr[element])
        
        if arr[element] < 0:
            negativos.append(arr[element])

        if arr[element] == 0:
            zeros.append(arr[element])

        pos = len(positivos) / n
        ngt = len(negativos) / n
        zer = len(zeros) / n

    return print('%.6f\n%.6f\n%.6f'%(pos,ngt,zer))

plusMinus([1, 2, 3, -1, -2, -3, 0,0])