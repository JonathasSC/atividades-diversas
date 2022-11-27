def catAndMouse(x, y, z):
    distanciaA = abs(x - z)
    distanciaB = abs(y - z)

    if distanciaA == distanciaB:
        return 'Mouse C'
    else:
        if distanciaB < distanciaA:
            return 'Cat B'
        else:
            return 'Cat A'

print(catAndMouse(2,5,4))