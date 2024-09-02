#!/usr/bin/python3
import sys  # Importation du module sys pour accéder aux arguments de la ligne de commande

# Définition d'une fonction récursive pour calculer la factorielle d'un nombre
def factorial(n):
    if n == 0:  # Condition de base : la factorielle de 0 est 1
        return 1
    else:  # Appel récursif : n * factorielle de (n-1)
        return n * factorial(n-1)

# Conversion du premier argument de la ligne de commande en entier
# Appel de la fonction factorielle avec cet argument
f = factorial(int(sys.argv[1]))

# Affichage du résultat de la factorielle
print(f)
