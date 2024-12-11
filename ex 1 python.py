#nom=input('Entrez votre nom ')
#prenom=input('Entrez votre prenom ')
#print(nom,prenom)

#num=int(input('Nombre  entier '))
#if num%2==0:
    #print('le nombre est pair')
#else :
    #print('le nombre est impair')

#num1=int(input('Nombre  entier '))
#if num1>0:
    #print(num1,'est un nombre positif')
#elif num1==0:
    #print(num1,'est un nombre nul')
#elif num1<0:
    #print(num1,'est un nombre négatif')

#print()

#for i in range(0,15,3):
    #print(i)

#print()

#for i in range(1,10):
   # print(i)
   # if i==8 :
    #    break


def contient_a(chaine):
    if 'a' in chaine:
        return "La chaîne contient le caractère 'a'."
    else:
        return "La chaîne ne contient pas le caractère 'a'."

chaine = input("Entrez une chaîne : ")
resultat = contient_a(chaine)
print(resultat)


