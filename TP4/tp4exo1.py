#Table de multiplication
x=float(input("Vous cherchez la table de multiplication de quel nombre ? "))
table=[]
for i in range(0,10):
    table.append([x,'*',i,'=',round(x*i,1)])
    print(table[i])