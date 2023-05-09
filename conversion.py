import random

def conversion(difficulty: int, _player):
    q1 = None
    responce = None
    listes = ['b', 'h', 'd']
    convertFrom = random.choice(listes)
    listes.remove(convertFrom)
    convertTo = random.choice(listes)
    daNumber = random.randint(0, difficulty)
    if convertFrom == 'b':
        q1 = bin(daNumber)[2:]
        if convertTo == 'h':
            responce = hex(daNumber)[2:]
        elif convertTo == 'd':
            responce = daNumber
    elif convertFrom == 'h':
        q1 = hex(daNumber)[2:]
        if convertTo == 'b':
            responce = bin(daNumber)[2:]
        elif convertTo == 'd':
            responce = daNumber
    elif convertFrom == 'd':
        q1 = daNumber
        if convertTo == 'b':
            responce = bin(daNumber)[2:]
        elif convertTo == 'h':
            responce = hex(daNumber)[2:]
    
    if convertTo == 'b':
        convert = 'binaire'
    elif convertTo == 'h':
        convert = 'hexadecimal'
    elif convertTo == 'd':
        d = 'decimal'

    userResponce = input(f"qu'elle est la conversion de {q1} en {convert} : ")
    try:
        if str(userResponce) == str(responce):
            print(f"bravo {_player}")
            return 1
        else :
            print(f"aïe, coup dure pour {_player}")
            return 0
    except ValueError:
        print('PETIT CON C DES PT DE NUMBRES QU IL FAUT RENTRER CONNARD')