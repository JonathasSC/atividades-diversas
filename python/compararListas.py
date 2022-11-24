participantes = {
    'alice':0,
    'bob':0
}

def compareTriplets(a,b):
    for pontos in range(0,3):
        if a[pontos] > b[pontos]:
            participantes['alice'] += 1
        if a[pontos] < b[pontos]:
            participantes['bob'] += 1
        else:
            pass        
    return list(participantes.values())

print(compareTriplets([17,28,30],[99,16,8]))