def recherche_indices_classement(elt, tab):
    result = [[], [], []]
    for i in range(len(tab)):
        if tab[i] == elt:
            result[1].append(i)
        elif tab[i] < elt:
            result[0].append(i)
        else:
            result[2].append(i)
    return result

print(recherche_indices_classement(3, [1, 3, 4, 2, 4, 6, 3, 0]))
# ([0, 3, 7], [1, 6], [2, 4, 5])
print(recherche_indices_classement(3, [1, 4, 2, 4, 6, 0]))
# print([0, 2, 5], [], [1, 3, 4])
print(recherche_indices_classement(3, [1, 1, 1, 1]))
# ([0, 1, 2, 3], [], [])
print(recherche_indices_classement(3, []))
# ([], [], [])


resultats = {
    'Dupont': {
        'DS1': [15.5, 4],
        'DM1': [14.5, 1],
        'DS2': [13, 4],
        'PROJET1': [16, 3],
        'DS3': [14, 4]
    },
    'Durand': {
        'DS1': [6 , 4],
        'DS2': [8, 4],
        'PROJET1': [9, 3],
        'IE1': [7, 2],
        'DS3': [12, 4]
    }
}

def moyenne(nom, resultats):
    '''Renvoie la moyenne de l'élève nom, selon le dictionnaire 
    resultats. Si nom n'est pas dans le dictionnaire, 
    la fonction renvoie None.'''
    if nom in resultats: 
        notes = resultats[nom]
        if len(notes) == 0: # pas de notes 
            return 0
        total_points = 0
        total_coefficients = 0
        for valeurs in notes.values(): 
            note, coefficient = valeurs
            total_points = total_points + note * coefficient 
            total_coefficients = total_coefficients + coefficient 
        return round( total_points / total_coefficients, 1 ) 
    else:
        return None

print(moyenne("Dupont", resultats))
# 14.5
print(moyenne("Durand", resultats))
# 8.5


