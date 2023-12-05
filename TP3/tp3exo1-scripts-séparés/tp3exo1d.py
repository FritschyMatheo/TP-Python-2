#Calcul et affichage du plus grand nombre N tel que ∑ 𝑖𝑁 𝑖=0 ≤ 𝑋 avec X un nombre supérieur à 1 saisit par l’utilisateur.
x=int(input("Entrer un nombre:"))
s2=0
total=0
while total<=x:
    N=s2
    s2+=1
    total+=s2
print(f"Le plus grand nombre N de la somme est: {N}")