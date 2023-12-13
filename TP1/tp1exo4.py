#Script de calcul du nombres de minutes écoulées depuis le début du mois en date
print("Saisir le nombre de minutes écoulées depuis le début du mois:")
min=input()
min=int(min)
minutes=min%60
hr=int(min/60)
heures=hr%24
jr=int(hr/24)
jours=jr
print(min, "minutes d'un mois représentent la date du" ,jours, "et l'heure : ",heures,":",minutes)