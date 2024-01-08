#Dictionnaires

dico = {"firstname": "Matheo","name": "FRITSCHY","promo": 2023,"group": "RT131"}

print(f"Votre nom est {dico['name']}, prénom est {dico['firstname']},vous faites partie de la promo {dico['promo']} et votre groupe est {dico['group']}")

dic = {"name": "toto","firstname": "titi","promo": 2022,"group": 202}

print("Les clés du dictionnaire sont :")
for i in dic.keys():
    print(f"-{i}")

print("Les valeurs du dictionnaire sont :")
for i in dic.values():
    print(f"-{i}")

print("Les tuplets du dictionnaire sont :")
for i in dic.items():
    print(f"-{i}")

dico2={"name": "tata","firstname": "tutu","promo": 2023,"group": 102}

binome = {1: dic,2: dico2}

print("Les étudiants formants le binôme sont :")
for i in binome.values():
    print(f"- L'étudiant {i['name']} {i['firstname']} du groupe {i['group']}")