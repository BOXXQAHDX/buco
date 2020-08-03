#быки и коровы

import random
import subprocess

def hidden_number ():
    '''генерирует случайное число 
    с неповторяюшимися числами'''
    numb = [0,1,2,3,4,5,6,7,8,9]
    numbr = random.choices (numb, k=3)
    if numbr[0] == numbr[1]:
        numbr = hidden_number ()
    elif numbr[0] == numbr[2]:
        numbr = hidden_number ()
    elif numbr[1] == numbr[2]:
        numbr = hidden_number ()
    else:
        return numbr

def player_input ():
    '''проверка ввода игрока'''
    player_numbr = input ('угадайте трех значное число: ')
    player_numbr = list(player_numbr)
    for i in range (len (player_numbr)):
        player_numbr[i] = int(player_numbr[i])
    if len (player_numbr) != 3:
        print ('что то не так. попробуйте ещё')
        player_numbr = player_input ()
    return player_numbr

def win_check (player_numbr, numbr):
    '''проверка на победу, быков, коров'''
    score = [0,0]
    if player_numbr == numbr:
        score[0] = 0
        score[1] = 3
        return score
    #коровы
    for i in numbr:
        for j in player_numbr:
            if i == j:
                score[0] += 1
    #быки
    for i in range (len(numbr)):
        if numbr[i] == player_numbr[i]:
            score[0] -= 1
            score[1] += 1
    return score

def play ():
    subprocess.call(['clear'])
    print ('''
┌───────────────┐┌───────────────────────────────┐
|Быки и к0р0вы  ||https://vk.com/termux_store    |└───────────────┘└───────────────────────────────┘
┌────────────────────────────────────────────────┐
|Правила - угадай число противника за меньшее    |
|количество попыток.                             |
|Противник будет давать подсказки:               |
|Коровы - числа не на своём местье               |
|Быки - числа на своём месте                     |
└────────────────────────────────────────────────┘
''')
    numbr = hidden_number ()
    for i in range (99999999999999):
        player_numbr = player_input ()
        score = win_check (player_numbr,numbr)
        if score[1] == 3:
            break
        print ('коровы - ',score[0])
        print ('быки - ',score[1])
        print ('──────────────────────────────────────────────────')
    print ('''┌────────────────────────────────────────────────┐
|Вы победили за ''',i,'''ходов                         |└────────────────────────────────────────────────┘''')
    print ('''┌────────────────────────────────────────────────┐|Обубликуйте ваш рекорд на                       |
|https://vk.com/termux_store                     |
└────────────────────────────────────────────────┘
''')

play ()



