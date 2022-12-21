# Un programme qui permet de determiner la tranche d'age d'une personne.
age = input("sasir votre age svp : \t")
age = int(age)
while age < 0:
    age = input("Veuiller sasir votre age correctement svp: \t")
    age = int(age)

if 0 < age < 18:
    print("vous êtes un(e) mineur(e).")
elif 18 <= age < 22:
    print("vous êtes majeur.")
elif 22 < age <= 40:
    print("Vous êtes un(e) adulte.")
else:
    print("vous êtes dans la generation ancienne.")
print("le test est terminer.")

