from random import *
from time import *
from threading import *
nb_de_tour = randint(0,15)
nb_sec = 0
def logique()-> int:
    score = 0
    for i in range(nb_de_tour):
        a = choice([0,1,"not 1","not 0"])
        b = choice([0,1,"not 1","not 0"])
        operateur = choice(["and","or","^"])            
        reponse = input(f"Que vaut {a} {operateur} {b} :")
        if reponse == str(int(eval(f'({a}) {operateur} ({b})'))):
            print("Woulo !")
            score += 1
        else :
            print(f"Mauvais résultat. C'était {(int(eval(f'({a}) {operateur} ({b})')))}")
    print(f"fin. ton score est de {score}")

def temps():
    global nb_sec
    while nb_sec < 10:
        logique()
        t = Thread(target=print, args=[nb_sec])
        t.run()
        sleep (1)

temps()
