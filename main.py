#comentário teste amigão

#>> Criar MATRIZ
# from ast import If

Lin = 1
Col = 1

matriz = {}
while Lin <= 9:
    while Col <= 9:
        matriz.update({str(Lin)+str(Col): ' '})
        Col += 1
    Col = 1
    Lin += 1

numeros_iniciais = {
    '16' : 5,
    '18' : 6,
    '19' : 4,
    '21' : 6,
    '22' : 1,
    '28' : 9,
    '31' : 2,
    '32' : 9,
    '33' : 4,
    '35' : 8,
    '36' : 3,
    '39' : 7,
    '45' : 2,
    '46' : 1,
    '47' : 7,
    '48' : 8,
    '51' : 1,
    '54' : 8,
    '56' : 4,
    '59' : 6,
    '62' : 2,
    '63' : 8,
    '64' : 7,
    '65' : 6,
    '71' : 4,
    '74' : 9,
    '75' : 7,
    '77' : 8,
    '78' : 3,
    '79' : 5,
    '82' : 7,
    '88' : 1,
    '89' : 9,
    '91' : 5,
    '92' : 3,
    '94' : 4
}

Lin = 1
Col = 1
while Lin <= 9:
    while Col <= 9:
        key = str(Lin)+str(Col)
        if key in numeros_iniciais :
            matriz.update({key : numeros_iniciais[key]})
        Col += 1
    Col = 1
    Lin += 1

blocos = {
    'bloco_1' : [11, 12, 13, 21, 22, 23, 31, 32, 33],
    'bloco_2' : [14, 15, 16, 24, 25, 26, 34, 35, 36],
    'bloco_3' : [17, 18, 19, 27, 28, 29, 37, 38, 39],
    'bloco_4' : [41, 42, 43, 51, 52, 53, 61, 62, 63],
    'bloco_5' : [44, 45, 46, 54, 55, 56, 64, 65, 66],
    'bloco_6' : [47, 48, 49, 57, 58, 59, 67, 68, 69],
    'bloco_7' : [71, 72, 73, 81, 82, 83, 91, 92, 93],
    'bloco_8' : [74, 75, 76, 84, 85, 86, 94, 95, 96],
    'bloco_9' : [77, 78, 79, 87, 88, 89, 97, 98, 99],
}

# for bloco, array in blocos.items():
#     if 91 in array :
#         print(bloco)
#         teste = bloco

# print(blocos[teste])


def NumeroValido(Cell, Num, Bloco):
    Lin = Cell[0]
    Col = Cell[1]
    x = 1
    
    for Cel_bloco in Bloco :
        if Num == matriz[str(str(Cel_bloco)[0])+str(str(Cel_bloco)[1])] :
            return False
    while x <= 9:
        if Num == matriz[str(Lin)+str(x)] :
            return False
        if Num == matriz[str(x)+str(Col)] :
            return False
        x += 1
    return True 

def VerificarBloco(Num):
    for bloco, array in blocos.items():
        if Num in array :
            return blocos[bloco]

#verificação
Lin = 1
Col = 1
while Lin <= 9:
    while Col <= 9:
        if(matriz[str(Lin)+str(Col)] == " "):
            Cell = str(Lin)+str(Col)
            Bloco = VerificarBloco(int(Cell))
            Num = 1
            while Num <= 9 :
                if NumeroValido(Cell, Num, Bloco) == True :
                    matriz[str(Lin)+str(Col)] = Col
                Num += 1
        Col += 1
    Col = 1
    Lin += 1




# daqui para baixo é só apresentação
a = 1
b = 1
c = 1
d = 1

while a <= 9:    
    line = ''
    while b <= 9:
        key = str(a)+str(b)
        if (b % 3) == 0 and b != 9 :
            line += " | " + str(matriz[key]) + " |"
        else:
            line += " | " + str(matriz[key])
        b += 1
    print(line + " |")
    
    if d == 3:
        print('\n')
        d = 0
    b = 1
    a += 1
    d += 1