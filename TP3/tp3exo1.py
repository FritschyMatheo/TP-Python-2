#Exercice a) Calcul de la somme des entiers naturels de la valeur entière
a=0
n=int(input("Entrez une valeur:"))
r=range(1,n+1)
for i in r:
    a=a+i
print(f"La somme des entiers contenus dans {n} est de: {a}")
#Exercice b) Boucle d’attente qui se termine si l’utilisateur entre la valeur 100
while True:
    n=int(input())
    if n==100:
        break
#Exercice c) Script de lecture de 10 valeurs qui doivent être entre 0 et 20