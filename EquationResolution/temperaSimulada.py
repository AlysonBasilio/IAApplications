import math
from random import randint
import random
import time

def getAptidao(State):
    f = 4*math.exp(-(State[0]**2+State[1]**2))+ \
        math.exp(-((State[0] - 5) ** 2 + (State[1] - 5) ** 2)) + \
        math.exp(-((State[0] + 5) ** 2 + (State[1] - 5) ** 2)) + \
        math.exp(-((State[0] - 5) ** 2 + (State[1] + 5) ** 2)) + \
        math.exp(-((State[0] + 5) ** 2 + (State[1] + 5) ** 2))
    return f

def aceptanceProbability(initialState,currentState,temp):
    if(getAptidao(currentState)<getAptidao(initialState)):
        return 1.0
    return math.exp((getAptidao(currentState)-getAptidao(initialState))/temp)

def temperaSimulada(initialState):
    temp = 1000000
    coolingRate = 0.0003
    k=0
    while temp > 1:
        currentState = [random.random() * randint(int(initialState[0]) - 10, int(initialState[0]) + 10),
                            random.random() * randint(int(initialState[1]) - 10, int(initialState[1]) + 10)]
        D_e = getAptidao(currentState) - getAptidao(initialState)
        if D_e>0:
            initialState[0]=currentState[0]
            initialState[1]=currentState[1]
        else:
            if math.exp(D_e/temp)<random.random():
                initialState[0] = currentState[0]
                initialState[1] = currentState[1]
        temp *= 1-coolingRate
        k+=1
    print('Iteracoes:', k)
    print('Max encontrado:',getAptidao(initialState))
    resultados.append(getAptidao(initialState))
    iteracoes.append(k)
    return

times = []
iteracoes = []
resultados = []
media = 0
mediaI = 0
for j in range(100):
    start_time = time.time()
    initialState = []
    for i in range(2):
        q = random.random()*randint(-10,10)
        initialState.append(q)
    # Aplicando solucao
    print(initialState)
    temperaSimulada(initialState)
    print(initialState)
    times.append(time.time() - start_time)
    print("--- %s seconds ---" %times[j])
    media += times[j]
    mediaI += iteracoes[j]
print("Media =",media/1000)
print("Iteracoes=",mediaI/1000)
a = -1
for i in range(len(resultados)):
    if resultados[i]>a:
        a = resultados[i]
print("Maior valor encontrado:",a)