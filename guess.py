mot = "bqnqne"
guess = ""

def createGuess(char, longueur):
    retour = char * longueur
    return retour

unMot = createGuess('-',  10)
unMot2 = createGuess('+',  10)
unMo3 = createGuess('_',  100)
print(unMot)
print(unMot2)
print(unMo3)

for caractere in unMot2:
    print(caractere)