#Table de multiplication
x=float(input("Vous cherchez la table de multiplication de quel nombre ? "))
m=0.0   #m est le résultat de la multiplication
table=[]
for i in range(0,10):
    table.append([x,'*',i,'=',round(x*i,1)])
    print(table[i])