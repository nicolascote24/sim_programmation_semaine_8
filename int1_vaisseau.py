# Listes des planètes et des distances en années-lumière
liste_planetes = ["Tatooine", "Hoth", "Endor", "Dagobah", "Naboo", "Kamino"]
liste_distances = [10.5, 4.2, 8.1, 6.7, 9.3, 7.8] # distances en années-lumière

# Variables du vaisseau
capacite_carburant = 100  # en litres
consommation_vaisseau = 3  # litres par année-lumière
consommation_equipage = 2  # unités de provisions par jour
vitesse_vaisseau = 2  # années-lumière par jour

# Fonction pour calculer le carburant nécessaire pour atteindre une planète
def calculer_carb_total():
    return 

# Fonction pour calculer les provisions nécessaires pour le voyage
def calculer_provision():
    return

# Fonction pour vérifier si le vaisseau peut atteindre une planète
def peut_atteindre_planete():
    return

# Fonction pour afficher les statistiques du vaisseau
def afficher_vaisseau():
    print("\n--- Caractéristiques du Vaisseau ---")
    #mettre les caractiéristique dans ici

# Programme principal
programme = True

while programme:
    print("\n--- Menu ---")
    print("1. Afficher les statistiques du vaisseau")
    print("2. Vérifier si le vaisseau peut atteindre une planète")
    print("3. Quitter")
        
    choix = input("Entrez votre choix (1-3) : ")
        
    if choix == "1":
        afficher_vaisseau()
    elif choix == "2":
        peut_atteindre_planete()

