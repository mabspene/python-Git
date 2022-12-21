import random
# un programme qui permet de deviner un nombre aléatoire

nb_aleatoire = 0
aleatoire = random.randrange(100)

while nb_aleatoire != aleatoire:
    nb_aleatoire = int(input("Deviner le nombre aléatoire qui est compris entre 0 et 100 >>\t"))
    if nb_aleatoire < aleatoire:
        print("le nombre saisi est plus petit que le nombre aléatoire.")
        continue
    elif nb_aleatoire > aleatoire:
        print("le nombre saisi est suppérieur au nombre aléatoire.")
        continue
    else:
        print("Félicitation vous avez gagner le nombre aléatoire est >>", aleatoire)
        break

print("au revoir à la prochaine.")

