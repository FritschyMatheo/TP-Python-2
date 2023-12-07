#Table de multiplication
x=float(input("Vous cherchez la table de multiplication de quel nombre ? "))
r=0.0   #r est le résultat de la multiplication
mult=[0,1,2,3,4,5,6,7,8,9]
table=[]
for i in range(0,10):
    table.append(round(mult[i]*x,1))
    print(f"{x} * {mult[i]} = {table[i]}")