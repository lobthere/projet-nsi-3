
import tkinter as tk
from tkinter import *   # Importation bibliothèque graphique
import time
from threading import Thread
from random import *

#Une fonction très simpliste pour l'exemple

reponse = ''


def calcul(type: int):

    def commencer():
        Thread(target=gestion_temps).start()


    def gestion_temps():
        nb_seconde = 0
        if type == 1:
            bouton_validation.config (command = conversion)
        #entree.bind("<Return>", lecture) #La fonction sera exécutée à chaque fois que l'utilisateur appuie sur "Entrée"
        while nb_seconde < 10:  # Teste si le temps est écoulé
            nb_seconde += 1
            time.sleep(1)
            zone_temps.config (text = nb_seconde)   # Affiche le temps écoulé
        bouton_validation.config(command = '') # Désactive appel de fonction
        print ("C'est fini")


    def conversion():
        global saisie
        valeur=randint(1, 16)
        zone_question.config (text = "Convertir "+str(valeur)+" décimal en binaire")
        saisie = reponse.get()
        print(saisie)


    fenetre = tk.Tk()
    fenetre.geometry('600x200')
    fenetre.title('Question')

    # Zone affichage temps
    zone_temps = tk.Label (text = 'Temps', fg = "red", font = ("Helvetica", 15), anchor = W)
    zone_temps.place (x = 10, y = 10)   # Positionne la zone

    # Zone bouton "Commencer"
    bouton_commencer = tk.Button (text = "Commencer")
    bouton_commencer.place(x = 100, y = 10)

    # Zone affichage question
    zone_question = tk.Label (text = "Cliquez", fg = "green", font = ("Helvetica", 20), anchor = W)
    zone_question.place (x = 10, y = 40)

    # Zone bouton de validation
    bouton_validation = tk.Button (text = "Valider")
    bouton_validation.place(x = 160, y = 75)

    # Zone saisie réponse
    reponse = tk.StringVar(fenetre)
    reponse.set('')
    saisie = tk.Entry(fenetre, textvariable=reponse, width=20)
    saisie.place (x = 10, y = 80)

    # Zone affichage bonne réponse
    bonne_réponse = tk.Label (text= "Bonne réponse", fg= "green" , font= ("Helvetica", 15), anchor= W)
    bonne_réponse.place (x=10, y=80)

    bouton_commencer.config (command = commencer)


    fenetre.mainloop()  # Boucle tant que la fenêtre n'est pas fermée
    return reponse


print(calcul(1))

