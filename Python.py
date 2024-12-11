# def contient_a(chaine):
#     if 'a' in chaine:
#         return "La chaîne contient le caractère 'a'."
#     else:
#         return "La chaîne ne contient pas le caractère 'a'."

# chaine = input("Entrez une chaîne : ")
# resultat = contient_a(chaine)
# print(resultat)

# def carre(x):
#     return x ** 2
# nombre = int(input("Entrez un nombre : "))
# resultat = carre(nombre)
# print(f"Le carré de {nombre} est {resultat}.")


import random
def somme():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    c = random.randint(1, 100)
    print(f"Les trois nombres générés sont : {a}, {b}, {c}")
    return a + b + c
resultat = somme()
print(f"La somme des trois nombres est : {resultat}")

