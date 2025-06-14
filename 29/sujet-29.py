def selection_enclos(animaux, num_enclos):
    result = []
    for animal in animaux:
        if animal["enclos"] == num_enclos:
            result.append(animal)
    return result

animaux = [ {'nom':'Medor', 'espece':'chien', 'age':5, 'enclos':2},
{'nom':'Titine', 'espece':'chat', 'age':2, 'enclos':5},
{'nom':'Tom', 'espece':'chat', 'age':7, 'enclos':4},
{'nom':'Belle', 'espece':'chien', 'age':6, 'enclos':3},
{'nom':'Mirza', 'espece':'chat', 'age':6, 'enclos':5}]


print(selection_enclos(animaux, 5))
[{'nom':'Titine', 'espece':'chat', 'age':2, 'enclos':5},
{'nom':'Mirza', 'espece':'chat', 'age':6, 'enclos':5}]
print(selection_enclos(animaux, 2))
[{'nom':'Medor', 'espece':'chien', 'age':5, 'enclos':2}]
print(selection_enclos(animaux, 7))
[]


def trouver_intrus(tab, g, d):
    """Renvoie la valeur de l'intrus situé entre les indices g et d 
    dans le tableau tab où :
    tab vérifie les conditions de l'exercice,
    g et d sont des multiples de 3."""
    if g == d:
        return tab[g]
    else:
        nombre_de_triplets = (d - g) // 3
        indice = g + 3 * (nombre_de_triplets // 2)
        if tab[indice] == tab[indice + 1]:
            return trouver_intrus(tab, indice + 3, d)
        else:
            return trouver_intrus(tab, g, indice)


print(trouver_intrus([3, 3, 3, 9, 9, 9, 1, 1, 1, 7,
2, 2, 2, 4, 4, 4, 8, 8, 8], 0, 18))
7
print(trouver_intrus([8, 5, 5, 5, 9, 9, 9, 18, 18, 18, 3, 3, 3],
0, 12))
8
print(trouver_intrus([5, 5, 5, 1, 1, 1, 0, 0, 0,
6, 6, 6, 3, 8, 8, 8], 0, 15))
3