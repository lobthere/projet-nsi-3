from tkinter import *   # Importation bibliothèque graphique
import time
from threading import Thread
from random import *
from tkinter import messagebox

def logitech():
    after_id = None

    #Une fonction très simpliste pour l'exemple

    reponse = ''

    # j'initialise la variable score
    global score
    score = 0



    def log(type: int):
        def commencer():
            Thread(target=gestion_temps).start()


        def gestion_temps():
            global score
            nb_seconde = 0
            if type == 1:
                bouton_validation.config (command = logique)
            #fenetre.bind('<Return>', lambda event : T()) #La fonction sera exécutée à chaque fois que l'utilisateur appuie sur "Entrée"
            while nb_seconde < 60:  # Teste si le temps est écoulé
                nb_seconde += 1
                time.sleep(1)
                zone_temps.config (text = nb_seconde)   # Affiche le temps écoulé
            bouton_validation.config(command = '') # Désactive appel de fonction
            print ("C'est fini")
            clicked()
            rec()
            time.sleep(3)
            if score != 0:
                score = 0
                scorelabel.config(text= "Your Score :" + str(score), bg= "powder blue")


        def logique()-> int:
            global score
            operateur = choice(["and","or","^"])
            a = choice([0,1,"not 1","not 0"])
            b = choice([0,1,"not 1","not 0"])
            if operateur == "^":
                b = choice([0,1])
            zone_question.config (text = "Que vaut "+str(a)+" "+str(operateur)+" "+str(b))
            reponse = eval(str(f'({a}){operateur}({b})'))
            if int(saisie.get()) == reponse:
                score = score + 1
                zone_resultat.configure(text="Très bien !")
                scorelabel.config(text= "Your Score :" + str(score), bg= "powder blue")
            else :
                zone_resultat.configure(text=f"C'est faux ! La réponse était {reponse}.")
                scorelabel.config(text= "Your Score :" + str(score), bg= "powder blue")
            delete_text()

        def stop():
            """ stop la minuteur """
            # Annule l'appel programmé à la minuterie
            global after_id
            if after_id is not None:
                zone_temps.after_cancel(after_id)
                after_id = None

        def fermeture():
            fenetre.destroy()

        def clicked():
                messagebox.showwarning('Fini', 'Temps écoulée. Lâche le clavier philipe. Je te vois continuer de loin. Tu te STOP')

        def rec():
            messagebox.askquestion('Recommencer','Est-ce que tu veux continuer mon grand')
            if "no":
                fermeture()
            if "yes":
                NONE

        fenetre = Tk()
        fenetre.geometry('1920x1080')
        fenetre.title('Question')

        #couleur du fond
        canvas = Canvas(fenetre, width = 1920, height = 1080)      
        canvas.pack()      
        img = PhotoImage(file="imports/nbg.png")      
        canvas.create_image(0,0, anchor=NW, image=img)  

        # Zone affichage temps
        zone_temps = Label (text = 'Temps', fg = "red", font = ("Helvetica", 15), anchor = W)
        zone_temps.place (x = 10, y = 10)   # Positionne la zone

        # Zone bouton "Commencer"
        bouton_commencer = Button (text = "Commencer")
        bouton_commencer.place(x = 200, y = 10)

        # Zone affichage question
        zone_question = Label (text = "Cliquez", fg = "green", font = ("Helvetica", 20), anchor = W)
        zone_question.place (x = 10, y = 40)

        # Zone bouton de validation
        bouton_validation = Button (text = "Valider")
        bouton_validation.place(x = 160, y = 85)

        # Zone saisie réponse
        reponse = StringVar(fenetre)
        reponse.set('')
        saisie = Entry(fenetre, textvariable=reponse, width=20)
        saisie.place (x = 10, y = 85)

        #indiquateur de score
        scorelabel = Label(text= "Your Score :" + str(score), bg= "powder blue")
        scorelabel.place(x=100, y=5, height= 35, width=100)

        # delete content from Text Box
        def delete_text():
            saisie.delete("0", "end")


        # Création d'un label pour afficher le résultat
        zone_resultat = Label(fenetre, text = "Zone résultat. " , bg ="white")
        zone_resultat.place(x = 10, y = 120)

        # Création d'un bouton Exit
        bouton_sortir = Button(fenetre, text = "Quitter", command = fermeture)
        bouton_sortir.place (x = 10, y = 150)



        bouton_commencer.config (command = commencer)

        fenetre.protocol("WM_DELETE_WINDOW", fermeture)
        fenetre.mainloop()  # Boucle tant que la fenêtre n'est pas fermée


    print(log(1))

