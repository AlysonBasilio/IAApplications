import pandas as pd
import math

def removeCityFromPath(city, path):
    print("Removendo ",city," do path")
    i=city
    for c in path:
        if city == c[0]:
            i = c
            # print(i)
            break
    path.remove(i)
    return path

def greedyPath(city1, city2):
    # Variavel que pega as cidades adjacentes a cidade que esta sendo visitada
    tmpAdjCities=[]
    # Variavel que guarda o caminho final
    path = []
    # Variavel auxiliar
    c = (city1, 0, tmpAdjCities)
    # Enquanto nao chegar a cidade destino...
    while c[0] != city2:
        # Compila-se todas as cidades adjacentes e suas respectivas distancias a cidade destino.
        for i in range(10):
            if(data['Adj'+str(i+1)][c] == ' '):
                break;
            else:
                tmpAdjCities.append((int(data['Adj'+str(i+1)][c]),
                                     getDistance(int(data['Adj'+str(i+1)][c]),city2),False))
        # print("-----------------")
        # Ordena-se as cidades pela distancia, da menor para a maior
        tmpAdjCities.sort(key=lambda tup: tup[1])
        print("Cidades adjacentes a ",c,": ",tmpAdjCities)
        # Variavel que verifica se entrou em um beco sem saída
        teste = False
        # Verifica se a cidade mais perto foi visitada. Se não, ela é adicionada ao caminho.
        # Se foi visitada, verifica a próxima cidade.
        for x in tmpAdjCities:
            if not x[2]:
                path.append((x[0],getDistance(c,x[0]),tmpAdjCities))
                c = x[0]
                visitedCities.append(c)
                teste = True
                break
        # Se todas as cidades adjacentes já foram visitadas, precisa-se remover a cidade atual do caminho
        # e pegar a próxima cidade
        if(not teste):
            # print("Cidade Atual = ",c," Cidade Anterior = ",path[len(path)-2][0])
            path = removeCityFromPath(c, path)
            c = path[len(path)-1][0]
        # print("Path: ", path)
        tmpAdjCities = []
    return path

def isIn(x, path):
    for tup in path:
        if x== tup[0]:
            return True
    return False

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

col = ['Coordinate x', 'Coordinate y', 'Adj1', 'Adj2', 'Adj3', 'Adj4',
        'Adj5', 'Adj6', 'Adj7', 'Adj8', 'Adj9', 'Adj10']
data = pd.read_csv('Uruguay.csv', sep = ';', names = col)

p = greedyPath(1, 10)
print(len(p))
# print(p)
print(calculateCostOfPath(p))
# for i in p:
#     print(i)