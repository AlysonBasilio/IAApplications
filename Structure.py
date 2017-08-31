import pandas as pd
import math

class City(object):
    """
    Node class store the data and the pointers to the next nodes (left and right).
    """

    def __init__(self, id, destiny):
        self.data = (id,getDistance(id,destiny))
        self.adjCities = []
        self.visited = False
        self.lastCity = None

class CityTree(object):
    """
    City tree class provides some methods to insert, remove and print the data.
    """

    def __init__(self, destiny):
        self.root = None
        self.destiny = destiny
        self.path = []
        self.visited = []

    def calcPath(self, idToInsert):
        new_node = City(idToInsert, self.destiny)
        if self.root is None:
            self.root = new_node
            self.root.visited = True
        node = self.root
        self.path.append(node)
        while int(node.data[0]) != self.destiny:
            if(len(node.adjCities)==0):
                node.adjCities = self.getAdjacentCities(node.data[0],self.destiny)
            visitedAllAdjCities = True
            for c in node.adjCities:
                if not c.visited:
                    if c.data[0] not in self.visited:
                        i = node.adjCities.index(c)
                        node.adjCities[i].visited = True
                        node.adjCities[i].lastCity = node
                        self.path.append(node.adjCities[i])
                        node = node.adjCities[i]
                        self.visited.append(node.data[0])
                        visitedAllAdjCities = False
                        break
            if visitedAllAdjCities:
                # print("Entrou para remocao", node.data[0],"Tamanho do path",len(self.path))
                self.visited.append(node.data[0])
                self.path.pop()
                node = self.path[-1]

    def alreadyVisited(self, id):
        # print("path")
        for c in self.path:
            # print(c.data[0], end='')
            if(id == c.data[0]):
                # print(id, "ja foi visitado")
                return True
        for c in self.visited:
            if(id == c):
                # print(id, "ja foi visitado")
                return True
        # print(id, "nao foi visitado")
        return False

    def getAdjacentCities(self, id, destiny):
        tmpAdjCities = []
        for i in range(10):
            if (data['Adj' + str(i + 1)][id] == ' '):
                break;
            else:
                if(not self.alreadyVisited(int(data['Adj' + str(i + 1)][id]))):
                    tmpAdjCities.append(City(int(data['Adj' + str(i + 1)][id]), destiny))
        tmpAdjCities.sort(key=lambda tup: tup.data[1])
        return tmpAdjCities

    def getPath(self):
        path = []
        node = self.path[-1]
        while node.lastCity is not None:
            path.append(node)
            node = node.lastCity
        return path

def getDistance(city1, city2):
    coordenades1 = [data['Coordinate x'][int(city1)],data['Coordinate y'][int(city1)]]
    coordenades2 = [data['Coordinate x'][int(city2)],data['Coordinate y'][int(city2)]]
    # print(coordenades1)
    # print(coordenades2)
    q1=float(coordenades1[0].replace(',','.'))-float(coordenades2[0].replace(',','.'))
    q2=float(coordenades1[1].replace(',','.'))-float(coordenades2[1].replace(',','.'))
    return math.sqrt(q1*q1+q2*q2)



col = ['Coordinate x', 'Coordinate y', 'Adj1', 'Adj2', 'Adj3', 'Adj4',
        'Adj5', 'Adj6', 'Adj7', 'Adj8', 'Adj9', 'Adj10']
data = pd.read_csv('Uruguay.csv', sep = ';', names = col)

p = CityTree(600)
p.calcPath(203)
print("Tamanho do caminho:",len(p.getPath()))
# for c in p.path:
#     print(c.data)
#     for x in c.adjCities:
#         print(x.data[0],end=' ')
#     print('\n')
# print(p)
# print(calculateCostOfPath(p))
# for i in p:
#     print(i)