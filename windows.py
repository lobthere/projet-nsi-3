from tkinter import *
from PIL import Image, ImageTk
from conversion_windows import *

_width = 500
_height = 500
color = 'gray'


"""___Le debut___"""
def conversion():
    surface.destroy()
    converion_window_tkt()

surface = Tk()
surface.title("Un jeu de memoire")

icone = Image.open('imports/logo.png')
icone2 = ImageTk.PhotoImage(icone)
surface.wm_iconphoto(False, icone2)

surface.configure(width=_width, height=_height, bg=color)
surface.geometry(f"{_width}x{_height}")

"""___le texte___"""
text_1 = Label(surface, text="Acceuil", bg=color, font=("Arial", 25))
text_1.place(anchor=CENTER, relx=.48, rely=.2)

"""__button___"""
b_arithmetique = Button(surface, text="arithmetique", command=None)
b_arithmetique.place(relx= .2, rely=.5)

b_conversion = Button(surface, text="conversion", command=conversion)
b_conversion.place(relx=.45, rely=.5)

b_logique = Button(surface, text="logique", command=None)
b_logique.place(relx=.7, rely=.5)

surface.mainloop()