import random
from time import sleep

def conversion(valueMax: int, _player, time):
    listes = ['bin', 'hex', 'int']
    convertFrom = random.choice(listes)
    listes.remove(convertFrom)
    convertTo = random.choice(listes)
    daNumber = random.randint(0, valueMax)
    try:
        q1 = eval(f'{convertFrom}({daNumber})')[2:]
    except TypeError:
        q1 = eval(f'{convertFrom}({daNumber})')
    try:
        convert = eval(f'{convertTo}({daNumber})')[2:]
    except TypeError:
        convert = eval(f'{convertTo}({daNumber})')

    try:
        userResponce = input(f"qu'elle est la conversion de {q1} ({convertFrom}) en {convertTo} : ")
        if str(userResponce) == str(convert):
            print(f"Bravo {_player}")
            return 1
        else :
            print(f"ton pere la pute {_player}")
            return -1
    except ValueError:
            print('You have a gros shnak')

if __name__ == '__main__':
    conversion(10, 'lobthere', 5)