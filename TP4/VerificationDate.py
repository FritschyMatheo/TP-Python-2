#Script qui détermine si la date entrée est valide ou non

while True:
    date=input("Entrez une date au format jjmmaaaa : ")
    if len(date)!=8:
        print("Mauvaise saisie.")
    else:
        j=int(date[0]+date[1])
        m=int(date[2]+date[3])
        a=int(date[4]+date[5]+date[6]+date[7])
        if m==2:
            if(((a%4==0) & (a%100!=0)| (a%400)) & (j > 28)):
                print(f"{date}, date incorrecte")
            elif j>29:
                print(f"{date}, date incorrecte")
            else:
                print("Date correcte")
                break
        elif (m > 12) | (j > 31):
                print("incorrecte")
        elif (1 <= m <= 7) & (m % 2 == 0) & (j > 30):
                print(f"{date}, date incorrecte")
        elif (8 <= m <= 12) & (m % 2 != 0) & (j > 30):
                print(f"{date}, date incorrecte")
        else:
            print("Date correcte")
            break