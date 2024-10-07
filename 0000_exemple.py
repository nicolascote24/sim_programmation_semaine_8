def carre(nombre):
    resultat = nombre * nombre
    return resultat

def multiplication(nombre1, nombre2):
    resultat = nombre1 * nombre2
    return resultat

def afficher_resultat(resultat1, resultat2):
    carre()
    print(f"résultat carre {resultat1} et résultat multiplication {resultat2}")

nb_user = int(input("entrez un nombre"))
nb_user2 = int(input("entrez un nombre"))

resultat = carre(nb_user)

resultat_multiplication = multiplication(nb_user, nb_user2)

afficher_resultat(resultat, resultat_multiplication)