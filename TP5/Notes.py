#Script de calcul de moyenne avec coefficiant et acceptation ou non

note=[]
s=0
coeff=0
v=True
msg="\n"

for i in range(2):
    valeur=input(f"Veuillez entrer la note du module {i} et le coefficient correspondant : ")
    note.append(valeur.split(" "))

for i in range(2):
    if float(note[i][0])<8:
        v=False
        msg+=f"Note {i} < 8\n"
    s+=float(note[i][0])*float(note[i][1])
    coeff+=float(note[i][1])
s=s/coeff
if (s<10):
    v=False
    msg+=f"Moyenne inférieure à 10 : {s:.2f}\n"

if v==True:
    print(f"Félicitations, vous passez l'année avec une moyenne de {s:.2f} !!")
else:
    print(f"Vous n'avez pas validé votre année car :\n{msg}")