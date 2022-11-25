# def staircase(n):
#     deg = 0
#     space = n
#     while deg < n+1:
#         print('⠀'*space,'#'*deg)
#         deg += 1
#         space -= 1
#     return
# staircase(6)

def staircase(n):
    for i in range(1,n+1):
        print(''.join(i*'#').rjust(n))
    return
staircase(6)
