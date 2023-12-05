#Script de lecture de 10 valeurs qui doivent être entre 0 et 20
inf10=0
entre10et15=0
sup15=0
n=1
v=20.1
for i in range(10):
    while v<0 or v>20:
        v=float(input(f"Donner la valeur {n}/10 entre 0 et 20:"))
    if v<10:
        inf10+=1
    elif v>=10 and v<15:
        entre10et15+=1
    else:
        sup15+=1
    n+=1
    v=20.1
print(f"Il y a {inf10} nombres inférieur(s) à 10, {entre10et15} compris entre 10 et 15 et {sup15} supérieur(s) à 15.")