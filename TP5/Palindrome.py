#Script test de palindrome (mots et phrases)

chaine=str.lower(input(f"Entrez un mot ou une phrase : "))
chainealpha=""

for i in range(len(chaine)):
    if chaine[i].isalpha():
        chainealpha+=chaine[i]

print(f"Version alphabétique : {chainealpha}")
i=0
while (i<len(chainealpha)/2-1 and chainealpha[i]==chainealpha[len(chainealpha)-1-i]):
    i+=1

if (i<len(chainealpha)/2-1):
    print("Ce n'est pas un palindrome.")
else:
    print("C'est un palindrome !")