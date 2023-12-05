#Jeu du nombre mystère
import random
x=random.randint(0,100)
essai=0
guess=-1
#print(f"{x}")
while guess!=x:
    guess=int(input("Essayez de deviner le nombre mystère: "))
    essai+=1
    if guess>x:
        print(f"Le nombre mystère est petit plus que {guess}")
    elif guess<x:
        print(f"Le nombre mystère est plus grand que {guess}")
    else:
        print(f"Vous avez trouvé le nombre mystère {x} en {essai} essai(s) !")