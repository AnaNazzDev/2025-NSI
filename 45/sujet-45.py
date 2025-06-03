def correspond(mot, mot_a_trou):
    replace = ""
    for m in range(len(mot_a_trou)):
        if mot_a_trou[m] == "*":
            replace += mot[m]
        else:
            replace += mot_a_trou[m]
    return (replace == mot)
    

print(correspond('INFORMATIQUE', 'INFO*MA*IQUE'))
# True
print(correspond('AUTOMATIQUE', 'INFO*MA*IQUE'))
# False
print(correspond('STOP', 'S*'))
# False
print(correspond('AUTO', '*UT*'))
# True


print("EX 2s")
def est_cyclique(plan):
    '''Prend en paramètre un dictionnaire `plan` correspondant à 
    un plan d'envoi de messages (ici entre les personnes A, B, C,
    D, E, F).
    Renvoie True si le plan d'envoi de messages est cyclique et 
    False sinon.'''
    expediteur = 'A'
    destinataire = plan[expediteur]
    nb_destinataires = 1

    while destinataire != expediteur:
        destinataire = plan[destinataire]
        nb_destinataires = nb_destinataires + 1

    return nb_destinataires == len(plan)


print(est_cyclique({'A':'E','F':'A','C':'D','E':'B','B':'F','D':'C'}))
# False
print(est_cyclique({'A':'E','F':'C','C':'D','E':'B','B':'F','D':'A'}))
# True
print(est_cyclique({'A':'B','F':'C','C':'D','E':'A','B':'F','D':'E'}))
# True
print(est_cyclique({'A':'B','F':'A','C':'D','E':'C','B':'F','D':'E'}))
# False