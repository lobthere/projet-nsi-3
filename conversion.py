import random

def conversion(valueMax: int, _player):
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
    userResponce = input(f"qu'elle est la conversion de {q1} en {convertTo} : ")

    try:
        if str(userResponce) == str(convert):
            print(f"Bravo {_player}")
            return 1
        else :
            print(f"aie, coup dure pour {_player}")
            return -1
    except ValueError:
            print('Value Error')