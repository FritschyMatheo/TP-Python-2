L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

mostfreq=0
f=0
fmax=0

for i in range(0, len(L1), 1):
    f=L1.count(L1[i])
    if fmax<f:
        fmax=f
        mostfreq=L1[i]

print(f"Le nombre le plus fréquent dans la liste est le : {mostfreq} ({fmax} x)")