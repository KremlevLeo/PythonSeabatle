import unicodedata
from random import randint


def playing_field(x):
    tmp_list = [[unicodedata.lookup('BLACK SQUARE')]*x for i in range(x)]
    return tmp_list


def print_playing_fild(playing_list):
    for i in playing_list:
        print(' '.join(list(map(str, i))))


def set_boat(x):
    botat_X_Y = []
    if x == 1:
        botat_X_Y = [0, 0]
    else:
        botat_X_Y = [randint(0, x-1), randint(0, x-1)]
    return botat_X_Y


def shot(boat):
    user_shot = []
    user_x = int(input('Enter coordinate X: '))
    user_shot.append(user_x-1)
    user_y = int(input('Enter coordinate Y: '))
    user_shot.append(user_y-1)
    if boat == user_shot:
        print('You win')
    else:
        print('You miss')
    return user_shot


def update(playing_list, shot):
    playing_list[shot[0]][shot[1]] = unicodedata.lookup('RADIOACTIVE SIGN')
    return playing_list
    

user_x = int(input("Введите размер игровлго поля: "))
playing_field_list = playing_field(user_x)
boat = set_boat(user_x)
print_playing_fild(playing_field_list)
user_shot = shot(boat)
playing_field_list = update(playing_field_list, user_shot)
print_playing_fild(playing_field_list)
