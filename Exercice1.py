nom = "Fritschy"
prenom = "Mathéo"
math = 16.5
anglais = 15.5
info = 17.25
promotion = 2023
moy = ( math + anglais + info) / 3

print("Les types des variables sont:")
print(type(nom),type(prenom),type(math),type(anglais),type(info),type(promotion))
#print((f"L'étudiant {nom} {prenom} de la promotion {promotion} a une moyenne de {moy:2f}"))
print("L'étudiant {} {} de la promotion {} a une moyenne de {:.2f}".format(nom,prenom,promotion,moy))
