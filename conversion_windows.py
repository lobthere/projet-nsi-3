from tkinter import *
from PIL import Image, ImageTk
import time

def converion_window_tkt():
    _width = 500
    _height = 500
    color = 'gray'
    _tmax = 6

    surface = Tk()
    surface.title("conversion")

    icone = Image.open('imports/logo.png')
    icone2 = ImageTk.PhotoImage(icone)
    surface.wm_iconphoto(False, icone2)

    surface.configure(width=_width, height=_height, bg=color)
    surface.geometry(f"{_width}x{_height}")


    """___les explications___"""

    txt_exp = Label(surface, text="complete le plus de bonne réponce avant la fin du temps imparti", bg=color, font=("Arial", 12))
    txt_exp.place(relx=.05, rely=.2)

    """___les fonctions___"""
    def printInput():
        global is_entered
        _input = get_reponce.get()
        get_reponce.delete(0, 'end')
        question_box.config(text=_input)

    def timer(tmax):
        global is_entered
        timer_txt.config(text=tmax)
        if tmax != 0:
            tmax = tmax - 1
            surface.after(1000, timer, tmax)
        else:
            timer_txt.config(text='temps écoulé')
            button_timer.place(relx=.4, rely=.5)

    def start_timer():
        timer(_tmax)
        button_timer.place(relx=25, rely=25)

    """___button___"""
    button_responce = Button(surface, text='Entrer', command=printInput)
    button_responce.place(relx=.5, rely=.6)

    button_timer = Button(surface, text='Start', command=start_timer)
    button_timer.place(relx=.4, rely=.5)


    """___le texte___"""
    text_1 = Label(surface, text="Conversion", bg=color, font=("Arial", 25))
    text_1.place(anchor=CENTER, relx=.48, rely=.1)

    timer_txt = Label(surface, text=_tmax, bg=color, font=('Arial', 25))
    timer_txt.place(relx=.1, rely=.35)

    question_box = Label(surface, text="prompt", bg=color, font=('Arial', 25))
    question_box.place(relx=.1, rely=.45)

    get_reponce = Entry(surface, width=15, font=('Arial', 15))
    get_reponce.place(relx=.1, rely=.6)

    surface.mainloop()

if __name__ == '__main__':
    converion_window_tkt()