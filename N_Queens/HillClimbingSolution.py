from random import randint
import time

def printTabuleiro():
    for i in range(n):
        for j in range(n):
            if(initialState[i]==j):
                print('Q', end='')
            else:
                print(' ', end='')
            print('|', end='')
        print('')
    return

def makeAMove(lastMove):
    i = randint(0,n-1)
    j = randint(0,n-1)
    if j==i:
        j = (j+1)%n
    t = (i,j)
    if t==lastMove:
        i = (i+1)%n
        j = (j + 1) % n
    aux = initialState[i]
    initialState[i] = initialState[j]
    initialState[j] = aux
    return (i,j)

def hillClimb(initialState):
    lastMove = (-1,-1)
    currentState = []
    for i in range(n):
        currentState.append(initialState[i])
    aptidao = getAptidao()
    k = 0
    # Calcular funcao de aptidao
    while aptidao != 1:
        initialState = []
        for i in range(n):
            initialState.append(currentState[i])
        lastMove = makeAMove(lastMove)
        aTemp = getAptidao()
        if aTemp>aptidao:
            aptidao = aTemp
            currentState = []
            for i in range(n):
                currentState.append(initialState[i])
        k+=1
        print("Iteracao: ",k)
    print('Iteracoes:', k)
    iteracoes.append(k)
    return

def getNumDeAtaques(i):
    a = 0
    # Check Principal Diagonal
    column = initialState[i]
    linha = i
    while linha != 0 and column != 0:
        linha = linha - 1
        column = column - 1
    for j in range(n):
        if (linha == n-1) or (column == n-1):
            break
        if initialState[linha] == column and linha != i:
            a+=1
        linha+=1
        column+=1

    # Check Secundary Diagonal
    column = initialState[i]
    linha = i
    while linha != 0 and column != n-1:
        linha = linha - 1
        column = column + 1
    for j in range(n):
        if (linha == n - 1) or (column == 0):
            break
        if initialState[linha] == column and linha != i:
            a+=1
        linha += 1
        column -= 1
    return a

def getAptidao():
    total = n*(n+1)
    a = 0
    for i in range(n):
        a+=getNumDeAtaques(i)
    return 1-a/total

# Numero de rainhas
n = 20
times = []
iteracoes = []
media = 0
mediaI = 0
start_time = time.time()
initialState = []
for i in range(n):
    q = randint(0,n-1)
    while q in initialState:
        q = randint(0, n - 1)
    initialState.append(q)
# Aplicando solucao
# printTabuleiro()
hillClimb(initialState)
# print("Solucao:")
# printTabuleiro()
times.append(time.time() - start_time)
# print("--- %s seconds ---" %times[j])
# media += times[j]
# mediaI += iteracoes[j]
print("Media =",media[0])
print("Iteracoes=",mediaI[0])

