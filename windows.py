from tkinter import *
from PIL import Image, ImageTk as tk
from conversion_windows import *
from calcul_logique_tkt_mon_reuf import *
from json import *


_width = 500
_height = 500
color = 'gray'
file = 'player.json'


"""___Le debut___"""
def conversion():
    surface.destroy()
    converion_window_tkt()

def logique():
    surface.destroy()
    logitech()

surface = Tk()
surface.title("Un jeu de memoire")

icone = tk.Image.open('imports/logo.png')
icone2 = ImageTk.PhotoImage(icone)
surface.wm_iconphoto(False, icone2)

surface.configure(width=_width, height=_height, bg=color)
surface.geometry(f"{_width}x{_height}")

"""___le texte___"""
text_1 = Label(surface, text="Acceuil", bg=color, font=("Arial", 25))
text_1.place(anchor=CENTER, relx=.48, rely=.2)

"""__base pour les pseudos et les scores___"""

with open(file) as user_player:
    user_content = load(user_player)


"""___les def___"""
def player_button():
    player_username = player.get()

    def check():
        a = user_content['users']
        for i in range(0, len(a), 1):
            if a[i]['player'] == player_username:
                c = True
            else:
                c = False
            if c == True:
                to_return = [c, a[i]]
                break
        if c == False:
            to_return = [c, None]
        return to_return
    
    does_exist = check()
    if does_exist[0] == True:
        score_of_player = does_exist[1]['score']
    else:
        score_of_player = []
    
    txt_to_save = f"['{player_username}', {score_of_player}, {does_exist[1]}]"

    to_save = open('info_to_load.txt', 'w')
    to_save.write(txt_to_save)

    b_logique.place(relx=.7, rely=.5)
    b_arithmetique.place(relx= .2, rely=.5)
    b_conversion.place(relx=.45, rely=.5)
    button_for_player.place(relx=25, rely=25)
    txt_for_player.place(relx=25, rely=25)
    player.place(relx=25, rely=25)


"""__button___"""
b_arithmetique = Button(surface, text="arithmetique", command=None)

b_conversion = Button(surface, text="conversion", command=conversion)

b_logique = Button(surface, text="logique", command=logique)

player = Entry(surface, width=15, font=('Arial', 15))
player.place(relx=.33, rely=.7)

txt_for_player = Label(surface, text='Entre ton nom étranger', bg=color, font=('Arial', 15))
txt_for_player.place(relx=.3, rely=.6)

button_for_player = Button(surface, text='Entrer', command=player_button)
button_for_player.place(relx=.7, rely=.7)

surface.mainloop()