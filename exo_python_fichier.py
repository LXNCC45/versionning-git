Resultat=[]
fichier=open("C:/Users/gasni/Desktop/fich.txt")
while True :
    ligne=fichier.readline()
    if ligne=="":
        break
    for mot in ligne.split():
        if mot.find('-')>=0:
            Resultat.append(float(mot))
        else:
            Resultat.append(int(mot))
fichier.close()
print(Resultat)

##def Fic(Fichier):
##    Resultat=[ ]
##    while True :
##        ligne=fichier.readline()
##        if ligne=="":
##            break
##        for mot in ligne.split():
##            if mot.find('.')>=0:
##                Resultat.append(float(mot))
##            else:
##                Resultat.append(int(mot))
##
