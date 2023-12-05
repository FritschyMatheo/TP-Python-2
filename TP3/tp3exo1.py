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
inf10=0
entre10et15=0
sup15=0
n=1
v=20.1
for i in range(10):
    while v<0 or v>20:
        v=float(input(f"Donner la valeur {n}/10 entre 0 et 20:"))
    if v<10:
        inf10+=1
    elif v>=10 and v<15:
        entre10et15+=1
    else:
        sup15+=1
    n+=1
    v=20.1
print(f"Il y a {inf10} nombres inférieur(s) à 10, {entre10et15} compris entre 10 et 15 et {sup15} supérieur(s) à 15.")
#Exercice d) Calcul et affichage du plus grand nombre N tel que ∑ 𝑖𝑁 𝑖=0 ≤ 𝑋 avec X un nombre supérieur à 1 saisit par l’utilisateur.
x=int(input("Entrer un nombre:"))
s2=0
total=0
while total<=x:
    N=s2
    s2+=1
    total+=s2
print(f"Le plus grand nombre N de la somme est: {N}")