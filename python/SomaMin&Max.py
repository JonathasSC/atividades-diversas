def miniMaxSum(arr):
    maximo = sum(arr) - min(arr)
    minimo = sum(arr) - max(arr)
    return print(minimo, maximo)
miniMaxSum([1,2,3,4,5])
#   for i in range(len(arr)):
        