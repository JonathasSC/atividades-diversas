# Tamanho da casa = s - t

# a = 0 
# d < 0 = esquerda
# d > 0 = direita

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    apple_unit = []
    orange_unit = []
    for i in apples:
        apple_unit.append(a+i)
    for j in oranges:
        orange_unit.append(b+j)
    no_of_apple = 0
    no_of_orange = 0
    for i in apple_unit:
        if i in range(s,t+1):
            no_of_apple += 1
    for i in orange_unit:
        if i in range(s,t+1):
            no_of_orange += 1
    print(no_of_apple)
    print(no_of_orange)