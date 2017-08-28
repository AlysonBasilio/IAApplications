import pandas as pd
import math

col = ['Coordinate x', 'Coordinate y', 'Adj1', 'Adj2', 'Adj3', 'Adj4',
        'Adj5', 'Adj6', 'Adj7', 'Adj8', 'Adj9', 'Adj10']
data = pd.read_csv('Uruguay.csv', sep = ';', names = col)

print (data.head())

def greedyPath(city1, city2):
    path = []
    tmpAdjCities=[]
    for i in range(10):
        if(data['Adj'+str(i+1)][city1] == ' '):
            break;
        else:
            tmpAdjCities.append([data['Adj'+str(i+1)][city1],getDistance(data['Adj'+str(i+1)][city1],city2)])
            print(data['Adj'+str(i+1)][city1])
    print(tmpAdjCities)
    return path

def getDistance(city1, city2):
    coordenades1 = [data['Coordinate x'][city1],data['Coordinate y'][city1]]
    coordenades2 = [data['Coordinate x'][city2],data['Coordinate y'][city2]]
    print(coordenades1)
    print(coordenades2)
    q1=float(coordenades1[0].replace(',','.'))-float(coordenades2[0].replace(',','.'))
    q2=float(coordenades1[1].replace(',','.'))-float(coordenades2[1].replace(',','.'))
    return math.sqrt(q1*q1+q2*q2)

greedyPath(2, 3)
