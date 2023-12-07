import re

def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("Division par zéro n'est pas autorisée.")
    return a / b

def calculatrice():
    historique = []

    while True:
        print("\nCalculatrice")
        print("1. Addition")
        print("2. Soustraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Afficher l'historique")
        print("6. Effacer l'historique")
        print("7. Quitter")

        choix = input("Choisissez une opération (1-7): ")

        if choix in ['1', '2', '3', '4']:
            try:
                nombre1 = float(input("Entrez le premier nombre : "))
                nombre2 = float(input("Entrez le deuxième nombre : "))
            except ValueError:
                print("Erreur : Veuillez entrer des nombres valides.")
                continue

            if choix == '1':
                resultat = addition(nombre1, nombre2)
                operation = f"{nombre1} + {nombre2} = {resultat}"
            elif choix == '2':
                resultat = soustraction(nombre1, nombre2)
                operation = f"{nombre1} - {nombre2} = {resultat}"
            elif choix == '3':
                resultat = multiplication(nombre1, nombre2)
                operation = f"{nombre1} * {nombre2} = {resultat}"
            elif choix == '4':
                try:
                    resultat = division(nombre1, nombre2)
                    operation = f"{nombre1} / {nombre2} = {resultat}"
                except ValueError as e:
                    print(f"Erreur : {e}")
                    continue

            print(f"Résultat : {resultat}")
            historique.append(operation)

        elif choix == '5':
            if not historique:
                print("Historique vide.")
            else:
                print("\nHistorique des opérations :")
                for operation in historique:
                    print(operation)

        elif choix == '6':
            historique = []
            print("Historique effacé.")

        elif choix == '7':
            print("Au revoir !")
            break

        else:
            print("Erreur : Choix invalide. Veuillez choisir une option valide.")

if __name__ == "__main__":
    calculatrice()
