#
x=float(input("Entrez un nombre décimal : "))
if ((x < -2 and -10 < x) or x == -2 or x == -10) or ((2 < x and x < 3) or x == 2) or ((0 < x and x < 1) or x == 1):
    print(f"{x} appartient à I")
else :
    print(f"{x} n'appartient pas à I")