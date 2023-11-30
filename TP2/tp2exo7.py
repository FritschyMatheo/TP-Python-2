#Script de simulation du lancement d'une pièce truquée sur pile
import random
piece=random.randint(0,2)
if piece < 1 or piece == 1 :
    print("Pile !")
else :
    print("Face !")