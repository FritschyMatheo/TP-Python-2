#Script de calcul d'ingredients pour une fondue fribourgeoise
BASE=4          #Indique le nombre de personnes pour lequel la recette est concue
fromage=800.0   #Quantité de fromage pour la recette de base (en grammes)
eau=2           #Quantité d'eau pour la recette de base (en decilitres)
ail=2           #Quantité d'ail pour la recette de base (en gousses)
pain=400        #Quantité de pain pour la recette de base (en grammes)
nbConvives=input("Entrez le nombre de personne(s) conviées à la fondue : ")



print(f"Pour faire une fondue fribourgeoise pour {nbConvives} personnes, il vous faut :\n- {fromage} gr de fromage\n- {eau} dl d'eau\n- {ail} gousse(s) d'ail\n- {pain} gr de pain")