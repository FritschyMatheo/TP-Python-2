#Affichage des nombres par ordre décroissant

#Version while
import time
n=int(input("Entrez un nombre entier positif: "))
while n>-1:
    print(f"{n}")
    n-=1
    time.sleep(1)