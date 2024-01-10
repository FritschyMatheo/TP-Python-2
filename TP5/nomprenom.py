#Script d'entrée de deux noms et prenoms qui classe par ordre

nom1=str.upper(input("Entrez le nom de la première personne : "))
prenom1=str.capitalize(input("Entrez le prenom de la première personne : "))
nom2=str.upper(input("Entrez le nom de la deuxième personne : "))
prenom2=str.capitalize(input("Entrez le prenom de la deuxième personne : "))

#print(type(nom1), type(prenom1))   Test si le type a bien été pris

print("Noms triés dans l'ordre :")
if (nom1 < nom2) or (nom1==nom2 and prenom1 < prenom2):
    print(f"{nom1} {prenom1}")
    print(f"{nom2} {prenom2}")
else:
    print(f"{nom2} {prenom2}")
    print(f"{nom1} {prenom1}")