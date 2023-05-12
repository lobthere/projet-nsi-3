import random
from time import sleep
from multiprocessing import Process

def conversion(valueMax: int, _player, time):
    def timer(_time):
        try:
            for i in range(_time, 0, -1):
                sleep(1)
            ValueError
        except OSError:
            None
    def question():
        try:
            userResponce = input(f"qu'elle est la conversion de {q1} ({convertFrom}) en {convertTo} : ")
            OSError
            return userResponce
        except ValueError:
            None

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
        p1 = Process(target=timer(time))
        p2 = Process(target=question)
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        userResponce = question()
        if str(userResponce) == str(convert):
            print(f"Bravo {_player}")
            return 1
        else :
            print(f"aie, coup dure pour {_player}")
            return -1
    except ValueError:
            print('Mince, tu n as plus de temps')

if __name__ == '__main__':
    conversion(10, 'lobthere', 5)