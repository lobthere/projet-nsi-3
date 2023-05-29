from tkinter import *

_width = 500
_height = 500
color = 'gray'

surface = Tk()
surface.title("conversion")
surface.configure(width=_width, height=_height, bg=color)
surface.geometry(f"{_width}x{_height}")

"""___le texte___"""
text_1 = Label(surface, text="Conversion", bg=color, font=("Arial", 25))
text_1.place(anchor=CENTER, relx=.48, rely=.2)

surface.mainloop()