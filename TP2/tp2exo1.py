#script de permutation de deux variables
print("Entrez une première valeur X :")
x=input()
print("Entrez une seconde valeur Y :")
y=input()
x=int(x)
y=int(y)
print(f"Avant la permutation X vaut {x} et Y {y}")
t=x
x=y
y=t
print(f"Après la permutation, X vaut {x} et Y {y}")