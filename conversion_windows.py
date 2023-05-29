from tkinter import *
from PIL import Image, ImageTk


def converion_window_tkt():
    _width = 500
    _height = 500
    color = 'gray'
    _tmax = 50

    surface = Tk()
    surface.title("conversion")

    icone = Image.open('imports/logo.png')
    icone2 = ImageTk.PhotoImage(icone)
    surface.wm_iconphoto(False, icone2)

    surface.configure(width=_width, height=_height, bg=color)
    surface.geometry(f"{_width}x{_height}")

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
            surface.after(10, timer, tmax)

    """___button___"""
    button_responce = Button(surface, text='Entrer', command=printInput)
    button_responce.place(relx=.5, rely=.6)


    """___le texte___"""
    text_1 = Label(surface, text="Conversion", bg=color, font=("Arial", 25))
    text_1.place(anchor=CENTER, relx=.48, rely=.2)

    timer_txt = Label(surface, text=_tmax, bg=color, font=('Arial', 25))
    timer_txt.place(relx=.1, rely=.35)

    question_box = Label(surface, text="prompt", bg=color, font=('Arial', 25))
    question_box.place(relx=.1, rely=.45)

    get_reponce = Entry(surface, width=15, font=('Arial', 15))
    get_reponce.place(relx=.1, rely=.6)

    surface.after(1000, timer, _tmax)
    surface.mainloop()

if __name__ == '__main__':
    converion_window_tkt()