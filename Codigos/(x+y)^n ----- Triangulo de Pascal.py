# -*- coding: utf-8 -*-
"""
Created on Thu May 27 11:00:56 2021

@author: BRUNO
"""

#Função que calcula (x+y)^n
def main():
    x = input('Digite o x: ')
    y = input('Digite o y: ')
    n = int(input('Digite o n: '))
    print('O resultado é: ')
    print(pascal(x,y,n))
def fat(n):
    resultado = 1
    for count in range (n):
        resultado *= (count+1)
    return resultado
def binomial(m,n):
    resultado = (fat(m))/(fat(n)*fat(m-n))
    return resultado
def pascal(x,y,n):
    pascal = []
    for cont in range (n+1):
        pascal.append(f'{int(binomial(n,cont))}*({x}^{n-cont}*{y}^{cont})')
    resultado = '+'.join(pascal)
    return resultado
if __name__ == '__main__':
    main()
    

















