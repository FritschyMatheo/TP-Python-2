#script de permutation de deux variables
x=input("Entrez  x: ")
y=input("Entrez  y: ")
x=int(x)
y=int(y)
print(f"Avant la permutation \nx : {x}\ny : {y}")
t=x
x=y
y=t
print(f"Après la permutation \nx : {x}\ny : {y}")