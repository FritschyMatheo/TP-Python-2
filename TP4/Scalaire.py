#Produit scalaire
nMax=3
scal=0.0
while True:
    n=int(input("Quelle est la taille de vos vecteurs [entre 1 et 3] ? "))
    if 1<=n and n<=nMax:
        break

v1=[0]*n
v2=[0]*n
print("Saisie du premier vecteur :")
for i in range(n):
    v1[i]=float(input(f"v1[{i}] = "))

print("\nSaisie du second vecteur :")
for i in range(n):
    v2[i]=float(input(f"v2[{i}] = "))

for i in range(n):
    scal=scal+v1[i]*v2[i]

print(f"\nLe produit scalaire de v1 par v2 vaut {scal}")