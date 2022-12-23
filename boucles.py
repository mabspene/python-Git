# Un programme qui permet de controler la saisie de l'utilisateur et afficher les nombres pairs comprisent entre 0 et ce nombre
nbr = int(input("saisir un nombre svp >> \t"))
while nbr < 0:
    nbr = input("saisir un nombre svp >> \t")
    nbr = int(nbr)
for i in range(1,nbr):
    if i % 2 == 0:
        print(i,"est in nombre pair.")