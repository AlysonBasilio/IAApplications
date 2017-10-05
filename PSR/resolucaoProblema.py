from random import randint
#Dominios

Cor_Casas = {'vermelha': False, 'amarela':False, 'azul':False, 'verde':False, 'marfim':False}
Posicao_Casas = {1:False,2:False,3:False,4:False,5:False}
Cigarros = {'Kool':False, 'Chesterfield':False, 'Winston':False, 'Lucky Strike':False, 'Parliament':False}
Bebidas = {'suco de laranja':False, 'chá':False, 'café':False, 'leite':False, 'água':False}
Animais = {'zebra':False, 'cachorro':False, 'raposa':False, 'caramujos':False, 'cavalo':False}
Variaveis = {'inglês':{ 'cor_casa':'',
                        'pos_casa':0,
                        'cigarro':'',
                        'bebida':'',
                        'animal':''},
             'espanhol':{ 'cor_casa':'',
                        'pos_casa':0,
                        'cigarro':'',
                        'bebida':'',
                        'animal':''},
             'noruegues':{ 'cor_casa':'',
                        'pos_casa':0,
                        'cigarro':'',
                        'bebida':'',
                        'animal':''},
             'ucraniano':{ 'cor_casa':'',
                        'pos_casa':0,
                        'cigarro':'',
                        'bebida':'',
                        'animal':''},
             'japones':{ 'cor_casa':'',
                        'pos_casa':0,
                        'cigarro':'',
                        'bebida':'',
                        'animal':''}}
DicionarioNac = {0:'inglês', 1:'espanhol', 2:'noruegues', 3:'ucraniano', 4:'japones'}
DicionarioVar = {0:'cor_casa', 1:'pos_casa', 2:'cigarro', 3:'bebida', 4:'animal'}
resolveu = False
#Funcao que retorna o dono daquela informacao
def getLinha(info, var, matriz):
    coluna = DicionarioVar.get(info)
    for i in range(5):
        if matriz[i][coluna]==var:
            return i

#Restricoes
#1>O inglês mora na casa vermelha
def rest1(matriz):
    if Cor_Casas['vermelha']:
        if matriz[0][0] != 'vermelha':
            return False
    else:
        if matriz[0][0] != '':
            return False
    return True
#2>O espanhol é dono do cachorro
def rest2(matriz):
    if Animais['cachorro']:
        if matriz[1][4] != 'cachorro':
            return False
    else:
        if matriz[1][4] != '':
            return False
    return True
#3>O norueguês mora na primeira casa à esquerda
def rest3(matriz):
    if Posicao_Casas[1]:
        if matriz[2][1] != 1:
            return False
    else:
        if matriz[2][1] != 0:
            return False
    return True
#4>Fumam-se cigarros Kool na casa amarela
def rest4(matriz):
    if Cor_Casas['amarela'] and Cigarros['Kool']:
        if getLinha('cor_casa', 'amarela', matriz) == getLinha('cigarro', 'Kool', matriz):
            return True
        else:
            return False
    else:
        if Cor_Casas['amarela']:
            if matriz[getLinha('cor_casa', 'amarela',matriz)][2] != '':
                return False
        else:
            if Cigarros['Kool']:
                if matriz[getLinha('cigarro', 'Kool',matriz)][0] != '':
                    return False
    return True
#5>O  homem  que  fuma  cigarros  Chesterfield  mora  na  casa ao  lado  do  homem que mora com a raposa
def rest5(matriz):
    if Cigarros['Chesterfield'] and Animais['raposa']:
        p1 = matriz[getLinha('cigarro', 'Chesterfield',matriz)][1]
        p2 = matriz[getLinha('animal', 'raposa',matriz)][1]
        if p1!=0 and p2!=0:
            p = p1-p2
            if p==1 or p==-1:
                return True
            else:
                return False
        else:
            return True
    return True
#6>O norueguês mora ao lado da casa azul
def rest6(matriz):
    if matriz[2][1] != 0 and Cor_Casas['azul'] and matriz[getLinha('cor_casa', 'azul',matriz)][1]!=0:
        p = matriz[2][1] - matriz[getLinha('cor_casa', 'azul',matriz)][1]
        if p==1 or p==-1:
            return True
        else:
            return False
    return True
#7>O fumante de cigarros Winston cria caramujos
def rest7(matriz):
    if Cigarros['Winston'] and Animais['caramujos']:
        if getLinha('cigarro', 'Winston',matriz)==getLinha('animal', 'caramujos',matriz):
            return True
        else:
            return False
    return True
#8>O fumante de cigarros Lucky Strike bebe suco de laranja
def rest8(matriz):
    if Cigarros['Lucky Strike'] and Bebidas['suco de laranja']:
        if getLinha('cigarro', 'Lucky Strike',matriz)==getLinha('bebida', 'suco de laranja',matriz):
            return True
        else:
            return False
    return True
#9>O ucraniano bebe chá
def rest9(matriz):
    if Bebidas['suco de laranja']:
        if getLinha('bebida', 'suco de laranja',matriz)== 3:
            return True
        else:
            return False
    return True
#10>O japonês fuma cigarros Parliament
def rest10(matriz):
    if Cigarros['Parliament']:
        if getLinha('cigarro', 'Parliament',matriz)== 4:
            return True
        else:
            return False
    return True
#11>Fumam-se cigarros Kool em uma casa ao lado da casa em que fica o cavalo
def rest11(matriz):
    if Cigarros['Kool'] and Animais['cavalo']:
        p1 = matriz[getLinha('cigarro', 'Kool',matriz)][1]
        p2 = matriz[getLinha('animal', 'cavalo',matriz)][1]
        if p1!=0 and p2!=0:
            p = p1 - p2
            if p==1 or p==-1:
                return True
            else:
                return False
    return True
#12>Bebe-se café na casa verde
def rest12(matriz):
    if Bebidas['café'] and Cor_Casas['verde']:
        if getLinha('bebida', 'café', matriz)==getLinha('cor_casa', 'verde',matriz):
            return True
        else:
            return False
    return True
#13>A casa verde está imediatamente à direita (à sua direita) da casa marfim
def rest13(matriz):
    if Cor_Casas['marfim'] and Cor_Casas['verde']:
        p1 = matriz[getLinha('cor_casa', 'verde',matriz)][1]
        p2 = matriz[getLinha('cor_casa', 'marfim',matriz)][1]
        if p1!=0 and p2!=0:
            p = p1-p2
            if p == 1:
                return True
            else:
                return False
    return True
#14>Bebe-se leite na casa do meio
def rest14(matriz):
    if Bebidas['leite'] and Posicao_Casas[3]:
        if getLinha('bebida', 'leite',matriz)==getLinha('pos_casa', 3,matriz):
            return True
        else:
            return False
    return True

def analiseRestricoes(matriz):
    if rest1(matriz) and rest3(matriz) and rest4(matriz) and rest5(matriz) and rest6(matriz) and rest7(matriz) and rest8(matriz) and rest9(matriz) and \
            rest10(matriz) and rest11(matriz) and rest12(matriz) and rest13(matriz) and rest14(matriz):
        return True
    else:
        return False

def construirResultado(matriz):
    Variaveis = {'inglês': {'cor_casa': matriz[0][0],
                            'pos_casa': matriz[0][1],
                            'cigarro': matriz[0][2],
                            'bebida': matriz[0][3],
                            'animal': matriz[0][4]},
                 'espanhol': {'cor_casa': matriz[1][0],
                            'pos_casa': matriz[1][1],
                            'cigarro': matriz[1][2],
                            'bebida': matriz[1][3],
                            'animal': matriz[1][4]},
                 'noruegues': {'cor_casa': matriz[2][0],
                            'pos_casa': matriz[2][1],
                            'cigarro': matriz[2][2],
                            'bebida': matriz[2][3],
                            'animal': matriz[2][4]},
                 'ucraniano': {'cor_casa': matriz[3][0],
                            'pos_casa': matriz[3][1],
                            'cigarro': matriz[3][2],
                            'bebida': matriz[3][3],
                            'animal': matriz[3][4]},
                 'japones': {'cor_casa': matriz[4][0],
                            'pos_casa': matriz[4][1],
                            'cigarro': matriz[4][2],
                            'bebida': matriz[4][3],
                            'animal': matriz[4][4]}}
    resolveu = True

# Algoritmo PSR
# DFS-recursive(G, s):
#         mark s as visited
#         for all neighbours w of s in Graph G:
#             if w is not visited:
#                 DFS-recursive(G, w)
def DFSrecursive(matriz,linha,coluna):
    if resolveu:
        return
    aux = []
    for i in range(5):
        aux.append([])
        for j in range(5):
            aux[i].append(matriz[i][j])
    i = randint(0,4)
    if coluna==0:
        keys = Cor_Casas.keys()
        while Cor_Casas[keys[i]]:
            i = randint(0,4)
        aux[linha][coluna] = keys[i]
    while
    aux[linha][coluna]
    Variaveis[DicionarioNac[linha]][DicionarioVar[coluna]] = True