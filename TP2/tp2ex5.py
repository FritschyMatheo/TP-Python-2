#Script expressions conditionnelles
n=input("Entrez un nombre entier: ")
n=int(n)
if n == 0 :
    print("Le nombre est zéro (et il est pair)")
elif n%2 == 0 :
    if n>0 :
        print("Le nombre est positif et pair")
    else :
        print("Le nombre est négatif et pair")
elif n>0 :
    print("Le nombre est positif et impair")
else :
    print("Le nombre est négatif et impair")