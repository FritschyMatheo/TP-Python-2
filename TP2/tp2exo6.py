#Script de simulation du lancement d'une pièce
import random
piece=random.randint(0,100)
if piece < 50 or piece == 50 :
    print("Pile !")
else :
    print("Face !")