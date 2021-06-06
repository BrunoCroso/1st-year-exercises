# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 09:06:57 2021

@author: BRUNO
"""

import matplotlib.pyplot as plt

#_______________________________________________________________________________________________________
#FUNÇÕES

def menu(lista1=[],lista2=[],n=0):
    print(70*'\033[1;34m_\033[m')
    print('')
    print('Os dados digitados foram:')
    if n == 0:
        print(lista1)
    if n == 1:
        print(f'''O primeiro conjunto de dados é: {lista1}
O segundo conjunto de dados é: {lista2}''')
    print(70*'\033[1;34m_\033[m')
    print('')
    print('\033[1;34mMENU\033[m'.center(80))
    print('''\033[1;34m0\033[m - Lista ordenada e número de elementos
\033[1;34m1\033[m - Média Aritimética
\033[1;34m2\033[m - Mediana
\033[1;34m3\033[m - Moda
\033[1;34m4\033[m - Variancia
\033[1;34m5\033[m - Desvio Padrão''')
    if n == 0:
        print('\033[1;34m6\033[m - Coeficiente de Variação ')
    if n == 1 and (len(lista1) == len(lista2)):
        print('\033[1;34m6\033[m - Coeficiemte de Correlação Linear de Pearson ')
        print('\033[1;34m7\033[m - Plotar grafico de pontos ')

    print('')
    if n == 0:
        print('\033[1;32m7 - REDIGITAR O CONJUNTO INICIAL DE DADOS\033[m')        
        print('\033[1;32m8 - DIGITAR MAIS UM CONJUNTO DE DADOS\033[m')
        print('\033[1;31m9 - SAIR DO SISTEMA\033[m')
    if n == 1:
        print('\033[1;32m8 - REDIGITAR O SEGUNDO CONJUNTO DE DADOS\033[m')        
        print('\033[1;31m9 - VOLTAR PARA O MENU INICIAL\033[m')
    print(70 * '\033[1;34m_\033[m')
    return('')


def transformador_de_lista (string):
    lista = []
    if string.count(',') == 0:
        lista_intermediaria = string.split()
        for contador in range (len(lista_intermediaria)):
            lista.append(float(lista_intermediaria[contador]))
    if string.count(',') > 0: 
        lista_intermediaria = string.split(',')
        for contador in range (len(lista_intermediaria)):
            lista.append(float(lista_intermediaria[contador]))
    return lista


def media(lista):
    media = 0
    for cont in range (len(lista)):
        media += lista[cont]
    media = media/(len(lista))
    return media

    
def mediana(lista):
    lista.sort()
    if len(lista) % 2 == 0:
        mediana = (lista[int(len(lista)/2)] + lista[(int(len(lista)/2)+1)])/2
    else:
        mediana = lista[int((len(lista)-1)/2)]
    return mediana
    


def moda(lista):
    moda = [lista[0]]
    elementos = 1
    lista.sort
    for cont in range(len(lista)):
        if lista.count(lista[cont]) > elementos:
            elementos = lista.count(lista[cont])
            moda = [lista[cont]]
        if (lista.count(lista[cont]) == elementos) and (moda.count(lista[cont]) == 0):
            moda.append(lista[cont])
    return moda

def elementos_da_moda(lista):
    moda = [lista[1]]
    elementos = 1
    lista.sort
    for cont in range(len(lista)):
        if lista.count(lista[cont]) > elementos:
            elementos = lista.count(lista[cont])
            moda = [lista[cont]]
        if (lista.count(lista[cont]) == elementos) and (moda.count(lista[cont]) == 0):
            moda.append(lista[cont])
    return elementos            


def variancia(lista):
    variancia = 0
    for c in range (len(lista)):
        media_lista = media(lista)
        variancia += ((lista[c] - media_lista)**2)
    variancia = variancia/len(lista)
    return variancia


def desvio_padrao(lista):
    desvio_padrao = variancia(lista) ** (1/2)
    return desvio_padrao

def coef_variação(lista):
    coef = (desvio_padrao(lista)/media(lista))*100
    return coef


def coef_linear(lista1,lista2):
    soma_dos_ZxZy = 0
    lista1_Z = []
    lista2_Z = []
    for c in range (len(lista1)):
        lista1_Z.append((lista1[c]-media(lista1))/desvio_padrao(lista1))
    for c in range (len(lista2)):
        lista2_Z.append((lista2[c]-media(lista2))/desvio_padrao(lista2))
    if len(lista1) == len(lista2):
        for c in range (len(lista1)):
            soma_dos_ZxZy += (lista1_Z[c]*lista2_Z[c])
        r = soma_dos_ZxZy/len(lista1)
        return r
    else:
        return ('\033[1;31mOs conjuntos de dados não tem o mesmo tamanho.\033[m')
            
#_____________________________________________________________________________________

dados = input('Diga o conjunto de dados: ')
try:
    dados = transformador_de_lista(dados)
except ValueError:
    print('\033[1;31mVocê digitou uma string.\033[m')
else:
    copia_dados = dados[:]
    copia_dados.sort()
    print (menu(dados))
    try:
        opção = int(input('Digite a opção desejada: '))
    except ValueError:
        print('\033[1;31mDigite um valor válido.\033[m')
        opção = int(input('Digite a opção desejada: '))
    if opção == 9:
        print(('\033[1;31mSaindo do sistema.\033[m'))
    
    while opção != 9:
        if opção == 0:
            print(f'''Os dados ordenados são:
{copia_dados}
O número de elementos da lista é {len(dados)}''')
        elif opção == 1:
            print(f'A média dos dados é {media(dados)}')
        elif opção == 2:
            print(f'A mediana dos dados é {mediana(dados)}')
        elif opção == 3:
            if len(moda(dados)) == 1:
                print(f'A moda dos dados é {moda(dados)} que apareceu {elementos_da_moda(dados)} vezes')
            if len(moda(dados)) > 1:
                print(f'As modas dos dados são {moda(dados)} que apareceram {elementos_da_moda(dados)} vezes cada')
        elif opção == 4:
            print(f'A variacia dos dados é {variancia(dados)}')
        elif opção == 5:
            print(f'O desvio padrão dos dados é {desvio_padrao(dados)}')
        elif opção == 6:
            print(f'O coeficiente de variação dos dados é de {coef_variação(dados)} %')
        elif opção == 7:
            dados = input('Redigite o conjunto de dados: ')
            dados = transformador_de_lista(dados)
            print(menu(dados))
#Novo conjunto de dados
        elif opção == 8:
            dados2 = input('Diga o novo conjunto de dados: ')
            try:
                dados2 = transformador_de_lista(dados2)
            except ValueError:
                print('\033[1;31mVocê digitou uma string.\033[m')
            else:
                copia_dados2 = dados2[:]
                copia_dados2.sort()
                print (menu(dados,dados2,1))
                try:
                    opção = int(input('Digite a opção desejada: '))
                except ValueError:
                    print('\033[1;31mDigite um valor válido.\033[m')
                    opção = int(input('Digite a opção desejada: '))
                if opção == 9:
                    print(('\033[1;31mVoltando para o menu inicial.\033[m'))
                    print(menu(dados))
                
                while opção != 9:
                    if opção == 0:
                        print(f'''Os dados ordenados do primeiro conjunto são:
{copia_dados}
O número de elementos da lista é {len(dados)}

Os dados ordenados do segundo conjunto são:
{copia_dados2}
O número de elementos da lista é {len(dados2)}''')

                    elif opção == 1:
                        print(f'A média do primeiro conjunto de dados é {media(dados)}')
                        print(f'A média do segundo conjunto de dados é {media(dados2)}')
                    elif opção == 2:
                        print(f'A mediana do primeiro conjunto de dados é {mediana(dados)}')
                        print(f'A mediana do segundo conjunto de dados é {mediana(dados2)}')

                    elif opção == 3:
                        if len(moda(dados)) == 1:
                            print(f'A moda do primeiro conjunto de dados é {moda(dados)}, que apareceu {elementos_da_moda(dados)} vezes')
                            if len(moda(dados2)) == 1:
                                print(f'A moda do segundo conjunto de dados é {moda(dados2)}, que apareceu {elementos_da_moda(dados2)} vezes')
                            if len(moda(dados2)) > 1:
                                print(f'As modas do segundo conjunto de dados são {moda(dados2)}, que apareceram {elementos_da_moda(dados2)} vezes cada')
                        if len(moda(dados)) > 1:
                            print(f'As modas do primeiro conjunto de dados são {moda(dados)}, que apareceram {elementos_da_moda(dados)} vezes cada')
                            if len(moda(dados2)) == 1:
                                print(f'A moda do segundo conjunto de dados é {moda(dados2)}, que apareceu {elementos_da_moda(dados2)} vezes')
                            if len(moda(dados2)) > 1:
                                print(f'As modas do segundo conjunto de dados são {moda(dados2)}, que apareceram {elementos_da_moda(dados2)} vezes cada')
                    elif opção == 4:
                        print(f'A variacia do primeiro conjunto de dados é {variancia(dados)}')
                        print(f'A variacia do segundo conjunto de dados é {variancia(dados2)}')

                    elif opção == 5:
                        print(f'O desvio padrão do primeiro conjunto de dados é {desvio_padrao(dados)}')
                        print(f'O desvio padrão do segundo conjunto de dados é {desvio_padrao(dados2)}')
                    elif opção == 6 and (len(dados) == len(dados2)):
                        print(f'O coeficiente de correlação linear de peearson entre os conjuntos é {coef_linear(dados,dados2)}')
                    elif opção == 7 and (len(dados) == len(dados2)):
                        plt.scatter(dados,dados2)
                        plt.show()
                    elif opção == 8:
                        dados2 = input('Redigite o segundo conjunto de dados: ')
                        dados2 = transformador_de_lista(dados2)
                        print(menu(dados,dados2,1))
                    else:
                        print('\033[1;31mDigite uma opção válida.\033[m')
                    opção = int(input('Digite a opção desejada: '))
                    if opção == 9:
                        print(('\033[1;31mVoltando para o menu inicial.\033[m'))
                        print (menu(dados))
                    

        else:
            print('\033[1;31mDigite uma opção válida.\033[m')
        opção = int(input('Digite a opção desejada: '))
        if opção == 9:
            print(('\033[1;31mSaindo do sistema.\033[m'))
