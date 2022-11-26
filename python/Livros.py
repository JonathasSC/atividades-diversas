def pageCount(n, p):
    livro = []
    for pag in range(n):
        livro.append(pag)
    print(livro)
    return n // p
    # if p % 2 == 0:
    #     return abs( n // p ) // p
    # else:
    #     return abs(( n // p ) // p - 1 )

print(pageCount(6,2))