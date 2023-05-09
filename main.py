import conversion
import timer

print("bonjour, bienvenue sur le programmme d'entrainenement au calcule mental")    #on dit bonjour au joueur

player_name = input("Choisit ton nom joueur : ")                                    #on retient son nom
print(f"Bonjour {player_name}")
pts = 0

while True:
        print("merci de selectionner votre programme : ")                                   #on l invite a selectionner le programme
        print("1- binaire hexadecimal decimal")
        print("2- booleens")
        print("3- arithmetique")
        print("4- fin du programme")
        possible_responce = ['1', '2', '3', '4']
        possible_responce_2 = ['1', '2', '3']
        programme = input("")
        if programme not in possible_responce:
            print("cette option n'est pas disponible")
        else :
            if programme == '1':
                _while = True
                responce = None
                while responce not in possible_responce_2:
                    print('choisit ta difficultee entre 1 et 3')
                    responce = input()
                    if responce == '1':
                        while _while:
                            r_c = conversion.conversion(10, player_name)
                            if r_c == 1:
                                pts = pts + r_c
                            print(f"votre nombre de points est de {pts}")
                            print('voulez vous continuez ? y/n')
                            r = input()
                            if r =='y':
                                None
                            elif r == 'n':
                                break
                            else :
                                break
                    elif responce == '2':
                         while _while:
                            r_c = conversion.conversion(100, player_name)
                            if r_c == 1:
                                pts = pts + r_c
                            print(f"votre nombre de points est de {pts}")
                            print('voulez vous continuez ? y/n')
                            r = input()
                            if r =='y':
                                None
                            elif r == 'n':
                                break
                            else:
                                break
                    elif responce == '3':
                        while _while:
                            r_c = conversion.conversion(1000, player_name)
                            if r_c == 1:
                                pts = pts + r_c
                            print(f"votre nombre de points est de {pts}")
                            print('voulez vous continuez ? y/n')
                            r = input()
                            if r =='y':
                                None
                            elif r == 'n':
                                break
                            else:
                                break
            elif programme == '2':
                print("ce n'est pas disponible pour l instant")
            elif programme == '3':
                print("ce n'est pas disponible pour l instant")
            elif programme == '4':
                print("fin du programme")
                break