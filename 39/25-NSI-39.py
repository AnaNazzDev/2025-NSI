def moyenne(notes):
    total = 0
    for n in notes:
        total += n
    return (total/len(notes)) if len(notes) > 0 else None

print(moyenne([5,3,8]))
# 5.333333333333333
print(moyenne([1,2,3,4,5,6,7,8,9,10]))
# 5.5
print(moyenne([]))
# Comportement différent suivant le traitement proposé. -> None


def tri(tab):
    '''tab est un tableau d'entiers contenant des 0 et des 1.
    La fonction trie ce tableau en plaçant tous les 0 à gauche'''
    i = 0 # premier indice de la zone non triée 
    j =  len(tab) - 1 # dernier indice de la zone non triée 
    while i < j:
        if tab[i] == 0:
            i = i + 1
        else:
            valeur = tab[i]   
            tab[j] = valeur
            tab[i] = 0
            j = j - 1

tab = [0,1,0,1,0,1,0,1,0]
tri(tab)
print(tab)
# [0, 0, 0, 0, 0, 1, 1, 1, 1]



