import conversion
import point

print("bonjour, bienvenue sur le programmme d'entrainenement au calcule mental")    #on dit bonjour au joueur

player_name = input("Choisit ton nom joueur : ")                                    #on retient son nom


while True:
        print("merci de selectionner votre programme : ")                                   #on l invite a selectionner le programme
        print("1- binaire hexadecimal decimal")
        print("2- booleens")
        print("3- arithmetique")
        print("4- fin du programme")
        possible_responce = ['1', '2', '3', '4']
        programme = input("")
        if programme not in possible_responce:
            print("cette option n'est pas disponible")
        else :
            if programme == '1':
                print("test")
            elif programme == '2':
                print("ce n'est pas disponible pour l instant")
            elif programme == '3':
                print("ce n'est pas disponible pour l instant")
            elif programme == '4':
                print("fin du programme")
                break