# Note /12

notes_classe = [{'Prénom':'Jacques', 'NSI':16, 'Maths':12}, {'Prénom' :'Anne', 'NSI':14, 'Maths':11},
 {'Prénom' :'Patrick', 'NSI':16, 'Maths':18}, {'Prénom' :'Joelle', 'NSI':12, 'Maths':10}]

# Question 1 Donnez le nombre d'enregistrements (1 pt) : 12

# Question 2 Donnez le type de la variable "notes_classe" (1 pt) : liste de dictionnaire

# Question 3 Donnez la liste des descripteurs (1 pt): Prénom, NSI, MATH

# Question 4 Donnez l'instruction permettant d’ajouter un enregistrement de votre choix (1 pt) : notes_classe[0]['un_enregistrement_de_votre_choix'] = 'un enregistrement de votre choix'

# Question 5 Achevez une fonction déterminant la moyenne obtenue dans une discipline comme par exemple NSI de la classe (4 pts) :

def calcule_moyenne(table, descripteur):
    moyenne_NSI = 0
    try:
        for i in range(0, len(table), 1):
            moyenne_NSI = moyenne_NSI + table[i].get(descripteur)
        return moyenne_NSI / len(table)
    except TypeError:
        print("ce descripteur n existe pas, veuillez verifier que ce descripteur existe bien")

moyenne_nsi = calcule_moyenne(notes_classe, 'NSI')
print("Moyenne: ", moyenne_nsi)


# Question 6 Créez une fonction "ajoute_moyenne_ligne(la_table)" qui ajoutant, à notre variable « table »,
# un nouveau descripteur « Moyenne » en prenant en paramètre notre variable "notes_classe"
# afin que notre table contienne la moyenne de chaque élève après exécution de la fonction
# résultat souhaité : [{'Prénom': 'Jean', 'NSI': 14, 'Maths': 16, 'Moyenne': 15.0}, { ... ] (4 pts) :

def ajoute_moyenne_ligne(table):
    rang = 0
    for enregistrement in table:
        somme = 0
        nb = 0
        for clé, valeur in enregistrement.items():
            if clé != "Prénom":
                nb = nb + 1
                somme = somme + valeur
        moyenne = somme / nb
        table[rang]['Moyenne'] = moyenne
        rang = rang + 1
    return table

notes_classe = ajoute_moyenne_ligne(notes_classe)
print("Notes classe + moyennes : ", notes_classe)

