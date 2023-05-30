from tkinter import *
from PIL import Image, ImageTk as tk
from conversion_windows import *
from calcul_logique_tkt_mon_reuf import *
import json


_width = 500
_height = 500
color = 'gray'


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

f_player_temp = open('player.json')
f_player_data = json.load(f_player_temp)

"""___les def___"""
def player_button():
    player_username = player.get()
    print(player_username)
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