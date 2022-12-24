import unicodedata
import os
from random import randint


def playing_field(x, y):
    tmp_list = [[unicodedata.lookup('BLACK SQUARE')]*x for i in range(y)]
    return tmp_list


def print_playing_fild(playing_list):
    for i in playing_list:
        print(' '.join(list(map(str, i))))


def set_boat(x, y):
    botat_X_Y = []
    if x & y == 1:
        botat_X_Y = [0, 0]
    else:
        botat_X_Y = [randint(0, x-1), randint(0, y-1)]
    return botat_X_Y


def shot(boat):
    user_shot = []
    user_x = int(input('Enter coordinate X: '))
    user_shot.append(user_x)
    user_y = int(input('Enter coordinate Y: '))
    user_shot.append(user_y)
    if boat == user_shot:
        print('You win')
    else:
        print('You miss')
    return user_shot


def update(playing_list, shot):
    playing_list[shot[0]][shot[1]] == unicodedata.lookup('RADIOACTIVE SIGN')
    

user_x = int(input("Введите ширину поля: "))
user_y = int(input("Введите высоту поля: "))
playing_field_list = playing_field(user_x, user_y)
boat = set_boat(user_x, user_y)
print_playing_fild(playing_field_list)
user_shot = shot(boat)
update(playing_field_list, user_shot)
print_playing_fild(playing_field_list)
