binome = ('login1', 'login2')
print(f"L’étudiant {binome[0]} est en binome avec l’étudiant {binome[1]}")

binome[1]=str(input("Tapez le login de votre nouveau binome :"))
del(binome[1])
binome[2] = "login3" 

#On ne peut pas agir sur les tuples