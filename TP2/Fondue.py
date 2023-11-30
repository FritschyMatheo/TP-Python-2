#Script de calcul d'ingredients pour une fondue fribourgeoise
BASE=4          #Indique le nombre de personnes pour lequel la recette est concue
fromage=800.0   #Quantité de fromage pour la recette de base (en grammes)
eau=2           #Quantité d'eau pour la recette de base (en decilitres)
ail=2           #Quantité d'ail pour la recette de base (en gousses)
pain=400        #Quantité de pain pour la recette de base (en grammes)
nbConvives=input("Entrez le nombre de personne(s) conviées à la fondue : ")
nbConvives=int(nbConvives)
fromageQuantite= fromage * nbConvives / BASE
eauQuantite= eau * nbConvives / BASE
ailQuantite= ail * nbConvives / BASE
painQuantite= pain * nbConvives / BASE

print(f"Pour faire une fondue fribourgeoise pour {nbConvives} personnes, il vous faut :\n- {fromageQuantite} gr de fromage\n- {eauQuantite} dl d'eau\n- {ailQuantite} gousse(s) d'ail\n- {painQuantite} gr de pain")