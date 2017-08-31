import pandas as pd
import math

def getDistance(city1, city2):
    coordenades1 = [data['Coordinate x'][int(city1)],data['Coordinate y'][int(city1)]]
    coordenades2 = [data['Coordinate x'][int(city2)],data['Coordinate y'][int(city2)]]
    # print(coordenades1)
    # print(coordenades2)
    q1=float(coordenades1[0].replace(',','.'))-float(coordenades2[0].replace(',','.'))
    q2=float(coordenades1[1].replace(',','.'))-float(coordenades2[1].replace(',','.'))
    return math.sqrt(q1*q1+q2*q2)

def calculateCostOfPath(path):
    cost = 0
    for c in path:
        cost += float(c[1])
    return cost

def isAdjacent(city1, city2):
    for i in range(10):
        x = data['Adj' + str(i + 1)][city1]
        if (x == ' '):
            return False
        else:
            if int(x)==city2:
                return True

def getAdjacentCities(id, destiny):
    tmpAdjCities = []
    for i in range(10):
        x = data['Adj' + str(i + 1)][id]
        if (x == ' '):
            break;
        else:
            tmpAdjCities.append((int(x), getDistance(int(x),destiny)))
    tmpAdjCities.sort(key=lambda tup: tup[1])
    return tmpAdjCities

def getPath(origem,destino):
    paths = {}
    c = origem
    distances = {}
    distances[c]=0
    estimated_distances = {}
    estimated_distances[origem] = getDistance(origem,destino)
    graph[origem][1]=True
    paths[c]=0
    while c!=destino:
        # print(c," - Distancia percorrida ate aqui - ",distances[c]," - Cidade anterior - ",paths[c])
        for i in graph[c][0]:
            dist_estim = distances[c]+getDistance(c,i[0])+i[1]
            print("Cidade",i[0],":",dist_estim,"=",distances[c],"+",getDistance(c,i[0]),"+",i[1])
            if estimated_distances.get(i[0]) is None:
                paths[i[0]] = c
                # print("cidade", i[0], "distancia estimada", dist_estim)
                estimated_distances[i[0]] = dist_estim
            elif dist_estim<estimated_distances[i[0]]:
                paths[i[0]] = c
                # print("cidade",i[0],"distancia estimada", dist_estim)
                estimated_distances[i[0]] = dist_estim
            # if not graph[i[0]][1]:
            #     print(i[0],"-",estimated_distances[i[0]])
        for item in sorted(estimated_distances, key=estimated_distances.get):
            if(not graph[item][1]):
                # print("\tDistancia estimada", item, "=", estimated_distances[item])
                distances[item] = distances[paths[item]]+getDistance(paths[item],item)
                c = item
                graph[item][1] = True
                break
    return paths

col = ['Coordinate x', 'Coordinate y', 'Adj1', 'Adj2', 'Adj3', 'Adj4',
        'Adj5', 'Adj6', 'Adj7', 'Adj8', 'Adj9', 'Adj10']
data = pd.read_csv('Uruguay.csv', sep = ';', names = col)

graph = {}
origem = 203
destino = 600
for i in range(len(data)):
    graph[i+1] = [getAdjacentCities(i+1,destino), False]

p = getPath(origem,destino)
x = destino
distancia = 0
while x != origem:
    print(str(p[x])+",",end=" ")
    distancia+=getDistance(x,p[x])
    x = p[x]
print("\n",distancia)