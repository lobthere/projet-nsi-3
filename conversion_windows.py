from tkinter import *
from PIL import Image, ImageTk
import time
import random
import json

def converion_window_tkt():
    _width = 500
    _height = 500
    color = 'gray'
    _tmax = 60
    global score
    score = 0

    """__on charge les fichiers___"""
    info_to_load = open('info_to_load.txt', 'r')
    info_to_load = info_to_load.read()
    info_to_load = info_to_load.replace('"', '')
    info_from_other_py_file = eval(info_to_load)
    player = info_from_other_py_file[0]
    player_score = info_from_other_py_file[1]
    

    surface = Tk()
    surface.title("conversion")

    icone = Image.open('imports/logo.png')
    icone2 = ImageTk.PhotoImage(icone)
    surface.wm_iconphoto(False, icone2)

    surface.configure(width=_width, height=_height, bg=color)
    surface.geometry(f"{_width}x{_height}")


    """___les explications___"""

    txt_exp = Label(surface, text="complete le plus de bonne réponse avant la fin du temps imparti", bg=color, font=("Arial", 12))
    txt_exp.place(relx=.05, rely=.2)

    """___les fonctions___"""

    def conversion():
        listes = ['bin', 'hex', 'int']
        convertFrom = random.choice(listes)
        listes.remove(convertFrom)
        convertTo = random.choice(listes)
        daNumber = random.randint(0, 100)
        try:
            q1 = eval(f'{convertFrom}({daNumber})')[2:]
        except TypeError:
            q1 = eval(f'{convertFrom}({daNumber})')
        try:
            convert = eval(f'{convertTo}({daNumber})')[2:]
        except TypeError:
            convert = eval(f'{convertTo}({daNumber})')
        
        userquestion = (f"qu'elle est la conversion de {q1} ({convertFrom}) en {convertTo} : ")
        convert = str(convert)
        liste = [userquestion, convert]
        return liste

    def timer(tmax):
        timer_txt.config(text=tmax)
        if tmax != 0:
            tmax = tmax - 1
            surface.after(1000, timer, tmax)
        else:
            timer_txt.config(text='temps écoulé')
            button_timer.place(relx=.4, rely=.5)
            button_responce.place(relx=25, rely=25)
            question_box.place(relx=25, rely=25)
            get_reponce.place(relx=25, rely=25)
            player_name.place(relx=25, rely=25)

            if info_from_other_py_file[2] == None:
                pass
            else:
                player_score.append(score)

                with open('player.json') as file:
                    content = json.load(file)
                
                for i in range(0, len(content['users']), 1):
                    if content['users'][i][player] == player:
                        c = True
                        to_save = content['users'][i]
                if c == True:
                    to_save[score] = player_score
                else:
                    content['users'] += {'player': player, 'score': player_score}

                with open('player.json', 'w') as test:
                    test.write(content)


    def start_timer():
        global r1
        global responce
        global question
        timer(_tmax)
        button_timer.place(relx=25, rely=25)
        button_responce.place(relx=.5, rely=.6)
        question_box.place(relx=.1, rely=.45)
        get_reponce.place(relx=.1, rely=.6)
        r1 = conversion()
        responce = r1[1]
        question = r1[0]
        question_box.config(text=question)

    def after():
        global r1
        global responce
        global question
        global score
        r2 = get_reponce.get()
        if r2 == responce:
            score += 1
            score_box.config(text=(f'score : {score}'))
        get_reponce.delete(0, 'end')

        r1 = conversion()
        responce = r1[1]
        question = r1[0]
        question_box.config(text=question)


    """___button___"""
    button_responce = Button(surface, text='Entrer', command=after)
    

    button_timer = Button(surface, text='Start', command=start_timer, font=('Arial', 25))
    button_timer.place(relx=.4, rely=.5)


    """___le texte___"""
    text_1 = Label(surface, text="Conversion", bg=color, font=("Arial", 25))
    text_1.place(anchor=CENTER, relx=.48, rely=.1)

    timer_txt = Label(surface, text=_tmax, bg=color, font=('Arial', 25))
    timer_txt.place(relx=.3, rely=.35)

    question_box = Label(surface, text="prompt", bg=color, font=('Arial', 15))
    
    get_reponce = Entry(surface, width=15, font=('Arial', 15))
    
    score_box = Label(surface, text=(f"score: {score}"), bg=color, font=('Arial', 15))
    score_box.place(relx=.1, rely=.8)

    player_name = Label(surface, text=f"player: {player}", bg=color, font=('Arial', 15))
    player_name.place(relx=.6, rely=.8)

    surface.mainloop()

if __name__ == '__main__':
    converion_window_tkt()