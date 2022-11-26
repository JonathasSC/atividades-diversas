def countingValleys(steps, path):
    vale = 0
    mar = 0
    for i in path:
        if i == "D" :
           mar -= 1
        else:
            mar += 1
            if mar == 0:
                vale += 1
            else:
                pass
    return vale

print(countingValleys(8,['U','D','D','D','U','D','U','U']))