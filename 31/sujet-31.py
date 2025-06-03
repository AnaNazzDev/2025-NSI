def recherche_motif(motif, chaine):
    indices = []
    if (motif not in chaine):
        return []
    n = len(motif)
    for i in range(len(chaine)):
        if chaine[i:i+n] == motif:
            indices.append(i)
    return indices


print(recherche_motif("ab", ""))
[]
print(recherche_motif("ab", "cdcdcdcd"))
[]
print(recherche_motif("ab", "abracadabra"))
[0, 7]
print(recherche_motif("ab", "abracadabraab"))
[0, 7, 11]


def parcours(adj, x, acc):
    '''Réalise un parcours en profondeur récursif
    du graphe donné par les listes d'adjacence adj 
    depuis le sommet x en accumulant les sommets
    rencontrés dans acc'''
    if x not in acc:
        acc.append(x)
        for y in adj[x]: 
            parcours(adj, y, acc) 

def accessibles(adj, x):
    '''Renvoie la liste des sommets accessibles dans le
    graphe donné par les listes d'adjacence adj depuis
    le sommet x.'''
    acc = []
    parcours(adj, x, acc)
    return acc


print(accessibles([[1, 2], [0, 3], [0], [1], [5], [4]], 0))
[0, 1, 3, 2]
print(accessibles([[1, 2], [0, 3], [0], [1], [5], [4]], 4))
[4, 5]
