#Calcul de la somme des entiers naturels de la valeur entière
a=0
n=int(input("Entrez une valeur:"))
r=range(1,n+1)
for i in r:
    a=a+i
print(f"La somme des entiers contenus dans {n} est de: {a}")