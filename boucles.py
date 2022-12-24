

""" Un programme qui permet de controler la saisie de l'utilisateur
 et afficher les nombres pairs comprisent entre 0 et ce nombre """

"""nbr = int(input("saisir un nombre svp >> \t"))
while nbr < 0:
    nbr = input("saisir un nombre svp >> \t")
    nbr = int(nbr)
for i in range(1, nbr):
    if i % 2 == 0:
        print("{} est un nombre pair.".format(i))"""

# un programme qui permet la saisie d'une valeur positif et determine
# la table de multiplication des valeurs comprises entre 1 et la la valeur saisie.

"""val = input("saisir un nombre svp>>\t")
val = int(val)
while val < 0:
    val = input("veuiller saisir un nombre positif>>\t")
    val = int(val)
for i in range(1, val):
    print("\n")
    print("la table de {} est:".format(i))
    for j in range(1, 12+1):
        print(">> {} x {} = {}".format(i, j, i*j))"""

# Un programme qui permet la saisie de 10 valeur et determine le maximum et le minimum
val = []
n = int(input("saisir le nombre de valeur à saisir svp >>\t"))
for i in range(n):
    val.append(int(input("saisir la valeur {} >>\t".format(i))))
for j in val:
    print("la valeur {} est {}".format(val.index(j), j))
print("le maximum est >>\t{}".format(max(val)))
print("le minimum est >>\t{}".format(min(val)))
