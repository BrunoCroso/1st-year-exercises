# -*- coding: utf-8 -*-
"""
Created on Mon May 31 19:20:29 2021

@author: BRUNO
"""

#JOGO DA FORCA

#Escolha da palavra
import random
import unidecode
faceis = ['Amarelo','Amiga','Amor','Ave','Avião','Avó','Balão','Bebê','Bolo','Branco','Cama','Caneca','Celular','Clube','Copo','Doce','Elefante','Escola','Estojo','Faca','Foto','Garfo','Geleia','Girafa','Janela','Limonada','Mãe','Meia','Noite','Óculos','Ônibus','Ovo','Pai','Pão','Parque','Passarinho','Peixe','Pijama','Rato','Umbigo']
dificeis = ['Acender','Afilhado','Ardiloso','Áspero','Assombração','Asterisco','Basquete','Caminho','Champanhe','Chiclete','Chuveiro','Coelho','Contexto','Convivência','Coração','Desalmado','Eloquente','Esfirra','Esquerdo','Exceção','Fugaz','Gororoba','Heterossexual','Horrorizado','Impacto','Independência','Modernidade','Oftalmologista','Otorrinolaringologista','Paralelepípedo','Pororoca','Prognósticio','Quarentena','Quimera','Refeição','Reportagem','Sino','Taciturno','Tênue','Visceral']
dificuldade = input('Qual a dificuldade desejada (F/D)? ')
while dificuldade != 'F' and dificuldade != 'f' and dificuldade != 'D' and dificuldade != 'd':
    print('\033[1;31mDigite uma dificuldade valida\033[m')    
    dificuldade = input('Qual a dificuldade desejada (F/D)? ')
if dificuldade == 'F' or dificuldade == 'f':
    palavra = faceis[random.randint(0,39)].upper()
elif dificuldade == 'D' or dificuldade == 'd':
    palavra = dificeis[random.randint(0,39)].upper()

#Definindo listas
acertos = []
erros = []
for cont in range (len(palavra)):
    acertos.append('_')


#O jogo
parada = 0
i = 0
while i < 8 and parada == 0:
    letra = (input('Diga uma letra: ')).upper()
    while len(letra) > 1:
        print('\033[1;31mDigite somente uma letra.\033[m')
        letra = (input('Diga uma letra: ')).upper()
    while letra == '':
        print('\033[1;31mNão foi digitado uma letra.\033[m')
        letra = (input('Diga uma letra: ')).upper()
    while acertos.count(letra) > 0 or erros.count(letra) > 0:
        print('\033[1;31mVocê digitou uma letra repetida. Tente novamente.\033[m')
        letra = (input('Diga uma letra: ')).upper()
    if unidecode.unidecode(palavra).count(letra) > 0:
        print('\033[1;32mACERTOU\033[m')
        for cont in range (len(palavra)):
            if unidecode.unidecode(palavra)[cont] == letra:
                acertos[cont] = palavra[cont]
        desenhos = (f'''
\t ________
\t|        |     \033[1;31m{erros}\033[m
\t|        
\t|        
\t|       
\t|       
\t|              {acertos}
\t|''',f'''
\t ________
\t|        |     \033[1;31m{erros}\033[m
\t|        O
\t|        
\t|       
\t|       
\t|              {acertos}
\t|''',f'''
\t ________
\t|        |     \033[1;31m{erros}\033[m
\t|        O
\t|        | 
\t|       
\t|       
\t|              {acertos}
\t|''',f'''
\t ________
\t|        |     \033[1;31m{erros}\033[m
\t|        O
\t|       /| 
\t|       
\t|       
\t|              {acertos}
\t|''',f'''
\t ________
\t|        |     \033[1;31m{erros}\033[m
\t|        O
\t|       /|\ 
\t|       
\t|       
\t|              {acertos}
\t|''',f'''
\t ________
\t|        |     \033[1;31m{erros}\033[m
\t|        O
\t|       /|\ 
\t|        /
\t|       
\t|              {acertos}
\t|''',f'''
\t ________
\t|        |     \033[1;31m{erros}\033[m
\t|        O
\t|       /|\ 
\t|        /\ 
\t|       
\t|              {acertos}
\t|''',f'''
\t ________
\t|        |     \033[1;31m{erros}\033[m
\t|        O
\t|       /|\ 
\t|       _/\ 
\t|       
\t|              {acertos}
\t|''',f'''
\t ________
\t|        |     \033[1;31m{erros}\033[m
\t|        O
\t|       /|\ 
\t|       _/\_
\t|       
\t|              {acertos}
\t|''')
        print(desenhos[i])
    else:
        print('\033[1;31mERROU\033[m')
        erros.append(letra)
        i += 1
        desenhos = (f'''
\t ________
\t|        |     \033[1;31m{erros}\033[m
\t|        
\t|        
\t|       
\t|       
\t|              {acertos}
\t|''',f'''
\t ________
\t|        |     \033[1;31m{erros}\033[m
\t|        O
\t|        
\t|       
\t|       
\t|              {acertos}
\t|''',f'''
\t ________
\t|        |     \033[1;31m{erros}\033[m
\t|        O
\t|        | 
\t|       
\t|       
\t|              {acertos}
\t|''',f'''
\t ________
\t|        |     \033[1;31m{erros}\033[m
\t|        O
\t|       /| 
\t|       
\t|       
\t|              {acertos}
\t|''',f'''
\t ________
\t|        |     \033[1;31m{erros}\033[m
\t|        O
\t|       /|\ 
\t|       
\t|       
\t|              {acertos}
\t|''',f'''
\t ________
\t|        |     \033[1;31m{erros}\033[m
\t|        O
\t|       /|\ 
\t|        /
\t|       
\t|              {acertos}
\t|''',f'''
\t ________
\t|        |     \033[1;31m{erros}\033[m
\t|        O
\t|       /|\ 
\t|        /\ 
\t|       
\t|              {acertos}
\t|''',f'''
\t ________
\t|        |     \033[1;31m{erros}\033[m
\t|        O
\t|       /|\ 
\t|       _/\ 
\t|       
\t|              {acertos}
\t|''',f'''
\t ________
\t|        |     \033[1;31m{erros}\033[m
\t|        O
\t|       /|\ 
\t|       _/\_
\t|       
\t|              {acertos}
\t|''')
        print(desenhos[i])
    if acertos.count('_') == 0:
        print('\033[1;32mPARABENS! VOCÊ GANHOU!\033[m')
        parada = 1
if i == 8:
    print('')
    print('\033[1;31mVOCÊ PERDEU!\033[m')
    print(f'A palavra buscada era {palavra.upper()}')



















