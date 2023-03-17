import random
import time

def conversion(valueMax, timer):
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
    t1 = time.time_ns()
    userResponce = input(f"qu'elle est la conversion de {q1} en {convertTo} : ")
    t2 = time.time_ns()
    print(t1)
    print(t2)
    print(t2-t1)
    if not(t2 - t1 > timer*10**9) or t2 - t1 == 0:
        try:
            if str(userResponce) == str(convert):
                print('bravo')
                Statement = True
            else :
                print('aïe, coup dure pour phillipe')
                Statement = False
        except ValueError:
            print('Value Error')
    else:
        print('tu as pris trop de temps pour repondre')
        Statement = False
    
    return Statement
    
conversion(1025, 60)