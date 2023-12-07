#Table de multiplication
x=float(input("Vous cherchez la table de multiplication de quel nombre ? "))
r=0.0   #r est le résultat de la multiplication
table=[]
for i in range(0,10):
    table.append(round(i*x,1))
    print(f"{x} * {i} = {table[i]}")