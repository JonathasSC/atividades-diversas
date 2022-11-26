def sockMerchant(n, ar):
    quantity = { c: ar.count(c) for c in set(ar) }.values()
    pares = 0 
    
    for element in quantity:
        if element % 2 == 0:
            pares += element
        else:
            pares += element - 1

    return pares // 2

print(sockMerchant(9,[10, 20, 20, 10, 10, 30, 50, 10, 20]))
