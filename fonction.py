from math import *
from donnee import *
from random import *
le_mot = ''
lettre = str()
def debut_prog():
    print("inserez votre pseudo")
    pseudo = input()
    print("votre pseudo est :{0}".format(pseudo))
    reponse()

def reponse():
    N = choice(mot_pendu)
    global le_mot 
    le_mot = N
    print(le_mot)
    print("commencez à réflechir")
    print("il y a {0} lettre".format(len(le_mot)))
    #enter_the_letter()
    jeux()

def enter_the_letter():
    # global lettre
    print("entrez une lettre")
    lettre = input(str())
    print("vous avez entrer {0}".format(lettre))
    return lettre;
    #jeux()

def jeux():
    global chance
    lettre = ""
    while chance > 0:
        lettre = enter_the_letter()
        if lettre in le_mot:
            print("cette lettre est dans le mot a l'emplacement{0}".format(le_mot.find(lettre)))
            
        else:
            chance = chance - 1
            print("FAUX!!!. Il vous reste {0} chance".format(chance))
            
debut_prog()







