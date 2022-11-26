def sockMerchant(n, ar):
    quantity = { c: ar.count(c) for c in set(ar) }
    pares = 0 
    for element in quantity.values():
        if element % 2 == 0:
            pares += element
        else:
            pares += element - 1

    return pares // 2

print(sockMerchant(9,[10, 20, 20, 10, 10, 30, 50, 10, 20]))
