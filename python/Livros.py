def pageCount(n, p):
    n = (n + 1) if n % 2 == 0 else n
    p = (p + 1) if p % 2 == 0 else p
    x = [int((p - 1)/2), int((n - p)/2)]
    
    return min(x)

print(pageCount(6,2))