import random
# un programme qui permet de deviner un nombre aléatoire

nb_aleatoire = int(input("Deviner le nombre aléatoire qui est compris entre 0 et 100 >>\t"))
aleatoire = random.randrange(100)
while nb_aleatoire != aleatoire:

    if nb_aleatoire < aleatoire:
        print("le nombre saisi est plus petit que le nombre aléatoire.")
        nb_aleatoire = int(input("Deviner le nombre aléatoire qui est compris entre 0 et 100 >>\t"))
        continue
    elif nb_aleatoire > aleatoire:
        print("le nombre saisi est suppérieur au nombre aléatoire.")
        nb_aleatoire = int(input("Deviner le nombre aléatoire qui est compris entre 0 et 100 >>\t"))
        continue
    else:
        print("Félicitation vous avez gagner le nombre aléatoire est >>", aleatoire)
        break

print("au revoir à la prochaine.")

