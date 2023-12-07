#Scrit de service de location de vélos
h1=0
h2=0
prix=0
print("Location de vélo :")
while True:
    debut=int(input("Donnez l’heure de début de la location (un entier) : "))
    fin=int(input("Donnez l’heure de fin de la location (un entier) : "))
    if debut>fin:
        print("Attention ! le début de la location est après la fin ...")
    elif debut==fin:
        print("Attention ! l’heure de fin est identique à l’heure de début.")

    elif debut>24 or debut<0 or fin>24 or fin<0:
        print("Les heures doivent être comprises entre 0 et 24 !")
    else:
        break
for i in range(debut,fin):
    if i>=7 and i<17:
        h2+=1
    else:
        h1+=1
prix=float(h2*2+h1)
print("Vous avez loué votre vélo pendant")
if h1>0:
    print(f"{h1} heure(s) au tarif horaire de 1.0 euro (s)")
if h2>0:
    print(f"{h2} heure(s) au tarif horaire de 2.0 euro (s)")
print(f"Le montant total à payer est de {prix} euro (s).")