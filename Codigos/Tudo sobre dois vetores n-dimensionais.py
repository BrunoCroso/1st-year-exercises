# -*- coding: utf-8 -*-
"""
Created on Sun May 30 18:36:06 2021

@author: BRUNO
"""

import math
vetor_A_junto = input('Diga o vetor A: ')
vetor_B_junto = input('Diga o vetor B: ')
vetor_A = []
vetor_B = []

if vetor_A_junto.count(',') == 0:
    vetor_A_intermediario = vetor_A_junto.split()
    for contador in range (len(vetor_A_intermediario)):
        vetor_A.append(int(vetor_A_intermediario[contador]))
if vetor_A_junto.count(',') > 0: 
    vetor_A_intermediario = vetor_A_junto.split(',')
    for contador in range (len(vetor_A_intermediario)):
        vetor_A.append(int(vetor_A_intermediario[contador]))
        
if vetor_B_junto.count(',') == 0:
    vetor_B_intermediario = vetor_B_junto.split()
    for contador in range (len(vetor_B_intermediario)):
        vetor_B.append(int(vetor_B_intermediario[contador]))
if vetor_B_junto.count(',') > 0: 
    vetor_B_intermediario = vetor_B_junto.split(',')
    for contador in range (len(vetor_B_intermediario)):
        vetor_B.append(int(vetor_B_intermediario[contador]))

dimensões = (len(vetor_A_intermediario))
produtoescalar = 0
modulo_vetor_A = 0
modulo_vetor_B = 0

if (len(vetor_A_intermediario)) != (len(vetor_B_intermediario)):
    print ('\033[1;31mERRO. Ambos os vetores devem ter o mesmo número de dimensões.\033[m')
else:
    for dimensão in range (dimensões):
        produtoescalar += vetor_A[dimensão] * vetor_B[dimensão]
    for dimensão in range (dimensões):
        modulo_vetor_A += (vetor_A[dimensão])**2
    modulo_vetor_A = modulo_vetor_A**(1/2)
    for dimensão in range (dimensões):
        modulo_vetor_B += (vetor_B[dimensão])**2
    modulo_vetor_B = modulo_vetor_B**(1/2)

    cos = (produtoescalar)/(modulo_vetor_A*modulo_vetor_B)
    try:
        angulo = math.acos(cos)
    except ValueError:
        cos = (math.trunc((produtoescalar)/(modulo_vetor_A*modulo_vetor_B)*10000)/10000)
        angulo = math.acos(cos)
    produtovetorial = modulo_vetor_A * modulo_vetor_B * math.sin(angulo)
    
    print('')
    print('\033[1;34mINFORMAÇÕES SOBRE OS VETORES:\033[m')
    print(f'\tO modulo do vetor A é {modulo_vetor_A}')
    print(f'\tO modulo do vetor B é {modulo_vetor_B}')
    print(f'\tO angulo entre os vetores (em radianos) é de {angulo} rad')
    print(f'\tO angulo entre os vetores (em graus) é de {math.degrees(angulo)} graus')
    print('\033[1;34mSOBRE O PRODUTO ESCALAR:\033[m')
    print(f'\tO produto escalar dos vetores é {produtoescalar}')
    print(f'\tO cosseno do angulo entre os vetores é {cos}')
    print('\033[1;34mSOBRE O PRODUTO VETORIAL:\033[m')
    print(f'\tA norma do produto vetorial é {produtovetorial}')
    print(f'\tO seno do angulo entre os vetores é {math.sin(angulo)}')
    if dimensões == 3:
        print('')
        continuar = input('Deseja realizar um produto misto (S/N)? ')
        if continuar == 'S' or continuar == 's':
            vetor_C_junto = input('Diga o vetor C: ')
            vetor_C = []
            modulo_vetor_C = 0
            if vetor_C_junto.count(',') == 0:
                vetor_C_intermediario = vetor_C_junto.split()
                for contador in range (len(vetor_C_intermediario)):
                    vetor_C.append(int(vetor_C_intermediario[contador]))
            if vetor_C_junto.count(',') > 0: 
                vetor_C_intermediario = vetor_C_junto.split(',')
                for contador in range (len(vetor_C_intermediario)):
                    vetor_C.append(int(vetor_C_intermediario[contador]))
            if (len(vetor_A_intermediario)) != (len(vetor_C_intermediario)):
                    print ('\033[1;31mERRO. Todos os vetores devem ter o mesmo número de dimensões.\033[m')
            else:
                for dimensão in range (dimensões):
                    modulo_vetor_C += (vetor_C[dimensão])**2
                determinantept1 = (vetor_A[0]*vetor_B[1]*vetor_C[2]) + (vetor_A[1]*vetor_B[2]*vetor_C[0]) + (vetor_A[2]*vetor_B[0]*vetor_C[1])
                determinantept2 = (vetor_A[2]*vetor_B[1]*vetor_C[0]) + (vetor_A[0]*vetor_B[2]*vetor_C[1]) + (vetor_A[1]*vetor_B[0]*vetor_C[2])
                produtomisto = determinantept1 - determinantept2
                print('')
                print('\033[1;34mSOBRE O PRODUTO MISTO:\033[m')
                print(f'\tO produto misto dos vetores ([A,B,C]) é {produtomisto}')
                print(f'\tO modulo do vetor C é {modulo_vetor_C}')
                if produtomisto == 0:
                    print('\tO conjunto {A,B,C} é LD')
                else:
                    print('\tO conjunto {A,B,C} é LI')
                