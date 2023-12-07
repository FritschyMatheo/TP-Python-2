#Factorielle itérative
b=int(input("Veuillez choisir la boucle à utiliser :\n1 : Boucle for\n2 : Boucle While\nChoix: "))              #choix de la boucle à effectuer pour obtenir la factorielle

while b!=1 and b!=2:                                                                                            #Test de validité de la valeur entrée
    b=int(input("La valeur entrée n'est pas correcte, veuillez effectuer le choix à nouveau: "))
if b==1:                                                                                                        #Test de la boucle selectionnée, ici boucle for
    print("La boucle For a été sélectionnée.")
    f=1
    n=int(input("Entrer le nombre dont on veut déterminer la factorielle: "))
    for i in range(1, n+1):
        f=f*i
        print(f"{f}")
    print(f"La factorielle de {n} est {f} !")

else:                                                                                                           #Boucle While
    print("La boucle While a été sélectionnée.")
    t=1
    f=1
    n=int(input("Entrer le nombre dont on veut déterminer la factorielle: "))
    while t < n+1:
        f=f*t
        t+=1
        print(f"{f}")
    print(f"La factorielle de {n} est {f} !")