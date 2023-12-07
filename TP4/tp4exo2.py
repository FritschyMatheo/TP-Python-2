#Script calcul de moyenne d'une ressource
nombreEtudiants=int(input("Donnez le nombre d'etudiants : "))
moyenne=0.0
notes=[]
total=0
for i in range(0,nombreEtudiants):
    t=float(input(f"Note etudiant {i} : "))
    notes.append(t)
    moyenne+=t
    total+=1
moyenne=moyenne/total
print(f"\nMoyenne de classe : {moyenne}\n")
print("Numéro de l’Etudiant | note | ecart a la moyenne")
for i in range(0,nombreEtudiants):
    print(f"{i} | {notes[i]} | {notes[i]-moyenne}")