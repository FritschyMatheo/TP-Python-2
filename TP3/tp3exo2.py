#Affichage des nombres par ordre décroissant
import time

#Version for
print("Boucle for")
n=int(input("Entrez un nombre entier positif: "))
for i in range(n,-1,-1):
    print(f"{n}")
    n-=1
    time.sleep(1)

#Version while
print("Boucle while")
n=int(input("Entrez un nombre entier positif: "))
while n>=0:
    print(f"{n}")
    n-=1
    time.sleep(1)