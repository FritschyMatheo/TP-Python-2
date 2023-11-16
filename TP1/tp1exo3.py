#Script de calcul du nombre de minutes écoulées dans le mois
print("Script de calcul du nombre de minutes écoulées dans le mois.")
print("Saisir le jour du mois:")
jours=input()
print("Saisir les heures:")
heures=input()
print("Saisir les minutes:")
minute=input()
jours=int(jours)
heures=int(heures)
minute=int(minute)
min=jours*1440+heures*60+minute
print(f"Depuis le début du mois, il s'est écoulé : {min} minutes !")