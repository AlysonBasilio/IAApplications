import pandas as pd
import math

class City:
    def __init__(self, id, destiny):
        self.id = id
        self.visited = False
        self.adjCities = []
        self.destiny = destiny

    def addAdjCity(self, id):
        if id in visited:
            return
        else:
            self.adjCities.append((City(id,self.destiny),getDistance(id, self.destiny)))
        # Ordena-se as cidades pela distancia, da menor para a maior
        self.adjCities.sort(key=lambda tup: tup[1])

def greedyPath(city1, city2):
    # Raiz da arvore do caminho
    c = int(city1)
    aux = City(int(city1), int(city2))
    aux.visited = True
    visited.append(city1)
    pilha = []
    while c != int(city2):
        print(c)
        c = int(c)
        for i in range(10):
            # print(i+1," ",data['Adj'+str(i+1)][c])
            if(data['Adj'+str(i+1)][c] == ' '):
                break;
            else:
                aux.addAdjCity(data['Adj'+str(i+1)][c])
        # print(aux.adjCities)
        allVerified = True
        for i in range(len(aux.adjCities)):
            if((not aux.adjCities[i][0].visited) and (aux.adjCities[i][0].id not in visited)):
                aux.adjCities[i][0].visited = True
                visited.append(aux.adjCities[i][0].id)
                pilha.append(aux.adjCities[i][0])
                allVerified = False
                aux = aux.adjCities[i][0]
                c = aux.id
                break
        if(allVerified):
            pilha.pop()
            # print(len(pilha))
            aux = pilha[len(pilha)-1]
            c = aux.id
    return pilha

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
    c1 = path[-1].id
    path.pop()
    while len(path)>0:
        c2 = path[-1].id
        cost += getDistance(c1,c2)
        c1 = c2
        path.pop()
    return cost

col = ['Coordinate x', 'Coordinate y', 'Adj1', 'Adj2', 'Adj3', 'Adj4',
        'Adj5', 'Adj6', 'Adj7', 'Adj8', 'Adj9', 'Adj10']
data = pd.read_csv('Uruguay.csv', sep = ';', names = col)
visited = []
p = greedyPath(203, 600)
print("Percurso: ",len(p))
print("Visitados: ",len(visited))
# print(p)
print(calculateCostOfPath(p))
for i in p:
    print(i)
print(getDistance(602,600))