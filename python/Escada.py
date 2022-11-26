def staircase(n):
    for i in range(1,n+1):
        print(''.join(i*'#').rjust(n))
    return
staircase(6)
