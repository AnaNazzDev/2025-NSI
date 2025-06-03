def couples_consecutifs(list):
    result = []
    for e in range(1, len(list)):
        if (list[e-1] == list[e]-1):
            result.append((list[e-1], list[e]))
    return result

print(couples_consecutifs([1, 4, 3, 5]))
# []
print(couples_consecutifs([1, 4, 5, 3]))
# [(4, 5)]
print(couples_consecutifs([1, 1, 2, 4]))
# [(1, 2)]
print(couples_consecutifs([7, 1, 2, 5, 3, 4]))
# [(1, 2), (3, 4)]
print(couples_consecutifs([5, 1, 2, 3, 8, -5, -4, 7]))
# [(1, 2), (2, 3), (-5, -4)]


def colore_comp1(M, i, j, val):
    if M[i][j] != 1:
        return

    M[i][j] = val

    if i-1 >= 0: # propage en haut
        colore_comp1(M, i-1, j, val)
    if i+1 < len(M): # propage en bas 
        colore_comp1(M, i+1, j, val) 
    if j-1 >= 0: # propage à gauche 
        colore_comp1(M, i, j-1, val) 
    if j+1 < len(M[0]): # propage à droite 
        colore_comp1(M, i, j+1, val)



M = [[0, 0, 1, 0], [0, 1, 0, 1], [1, 1, 1, 0], [0, 1, 1, 0]]
print(M)
# [[0, 0, 1, 0], [0, 3, 0, 1], [3, 3, 3, 0], [0, 3, 3, 0]]