# -*- coding: utf-8 -*-
"""
Created on Mon May 24 10:58:14 2021

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
cos = 0

if (len(vetor_A_intermediario)) != (len(vetor_B_intermediario)):
    print ('ERRO. Ambos os vetores devem ter o mesmo número de dimensões.')
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
    angulo = math.acos(cos)
    
    print(f'O produto escalar dos angulos é {produtoescalar}')
    print(f'O modulo do vetor A é {modulo_vetor_A}')
    print(f'O modulo do vetor B é {modulo_vetor_B}')
    print(f'O cosseno do angulo entre os vetores é {cos}')
    print(f'O angulo entre os vetores (em radianos) é de {angulo} rad')
    print(f'O angulo entre os vetores (em graus) é de {math.degrees(angulo)} graus')
    
    
    
    
    
    
    
