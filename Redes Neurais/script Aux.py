
file = open("Rio 01 Camargos.txt", "r")
data = file.read()
river1_temp = data.split("\n")
river1 = []
for ano in river1_temp:
    river1 += ano.split('\t')
print(len(river1))
for i in range(len(river1)):
    print("Mês",i,":",river1[i])
file.close()
from sklearn.neural_network import MLPRegressor
