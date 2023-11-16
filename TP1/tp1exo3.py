#Script de calcul du nombre de minutes écoulées dans le mois
print("Script de calcul du nombre de minutes écoulées dans le mois.")
print("Saisir le jour du mois:")
jour=input()
print("Saisir les heures:")
heures=input()
print("Saisir les minutes:")
minute=input()
jour=int(jour)
heures=int(heures)
minute=int(minute)
min=jour*1440+heures*60+minute
print(f"Depuis le début du mois, il s'est écoulé : {min} minutes !")