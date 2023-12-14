L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Completez le programme a partir d'ici.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""
mostfreq=0
f=0
fmax=0

for i in range(0, len(L1), 1):
    for j in range(1, len(L1), 1):
        if L1[i] == L1[j]:
            f+=1
        if fmax<f:
            fmax=f
            mostfreq=L1[i]
    f=0

print(f"Le nombre le plus fréquent dans la liste est le : {mostfreq} ({fmax} x)")

""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Ne rien modifier apres cette ligne.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""
