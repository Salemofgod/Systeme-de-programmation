def factoriel(n):
    resultat = 1
    for i in range(1, n + 1):
        resultat = resultat * i
    return resultat

# Exemple d'utilisation
nombres = [3, 5, 7, 10]
for n in nombres:
    print(f"Factoriel de {n} = {factoriel(n)}")