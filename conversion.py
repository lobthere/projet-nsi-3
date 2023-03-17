import random

def conversion():
    q1 = None
    responce = None
    listes = ['b', 'h', 'd']
    convertFrom = random.choice(listes)
    listes.remove(convertFrom)
    convertTo = random.choice(listes)
    daNumber = random.randint(0, 1025)
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
            print('bravo')
        else :
            print('aïe, coup dure pour phillipe')
    except ValueError:
        print('PETIT CON C DES PT DE NUMBRES QU IL FAUT RENTRER CONNARD')
    
conversion()