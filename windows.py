from tkinter import *
import conversion_windows

_width = 500
_height = 500
color = 'gray'


"""___Le debut___"""
def conversion():
    surface.destroy()
    conversion_srf = Tk()
    conversion_srf.title("conversion")
    conversion_srf.configure(width=500, height=500, bg=color)
    conversion_srf.geometry('500x500')
    conversion_srf.mainloop()

surface = Tk()
surface.title("Un jeu de memoire")
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