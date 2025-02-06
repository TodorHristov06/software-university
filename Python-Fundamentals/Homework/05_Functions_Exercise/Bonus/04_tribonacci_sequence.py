def printTribRec(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1 
    elif n == 2:
        return 2
    else:
        return printTribRec(n - 1) + printTribRec(n - 2) + printTribRec(n - 3)

def printTrib(n):
    for i in range(n):
        print(printTribRec(i), end=" ")

n = int(input())
printTrib(n)