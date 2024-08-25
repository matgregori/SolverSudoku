#comentário teste amigão

#>> Criar MATRIZ
a = 1
b = 1

matriz = {}
while a <= 9:
    while b <= 9:
        matriz.update({str(a)+str(b): ' '})
        b += 1
    b = 1
    a += 1

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

a = 1
b = 1
while a <= 9:
    while b <= 9:
        key = str(a)+str(b)
        if key in numeros_iniciais :
            matriz.update({key : numeros_iniciais[key]})
        b += 1
    b = 1
    a += 1


#print(matriz)

bloco_1 = {'ini' : 11, 'fim' : 33}
bloco_2 = {'ini' : 14, 'fim' : 36}
bloco_3 = {'ini' : 17, 'fim' : 39}
bloco_4 = {'ini' : 41, 'fim' : 63}
bloco_5 = {'ini' : 44, 'fim' : 66}
bloco_6 = {'ini' : 47, 'fim' : 69}
bloco_7 = {'ini' : 71, 'fim' : 93}
bloco_8 = {'ini' : 74, 'fim' : 96}
bloco_9 = {'ini' : 77, 'fim' : 99}


#exit()

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