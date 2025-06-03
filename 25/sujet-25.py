def annee_temperature_minimale(t_moy, annees):
    mini = t_moy[0]
    mini_a = annees[0]
    for i in range(len(t_moy)):
        if t_moy[i] < mini:
            mini = t_moy[i]
            mini_a = annees[i]
    return (mini, mini_a)

t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]
print(annee_temperature_minimale(t_moy, annees))


def inverse_chaine(chaine):
    '''Retourne la chaine inversée'''
    resultat = ""
    for caractere in chaine:
        resultat = caractere + resultat 
    return resultat

def est_palindrome(chaine):
    '''Renvoie un booléen indiquant si la chaine ch
    est un palindrome'''
    inverse = inverse_chaine(chaine)
    return inverse == chaine

def est_nbre_palindrome(nbre):
    '''Renvoie un booléen indiquant si le nombre nbre 
    est un palindrome'''
    chaine = str(nbre)
    return est_palindrome(chaine)

print(inverse_chaine('bac'))
'cab'
print(est_palindrome('NSI'))
False
print(est_palindrome('ISN-NSI'))
True
print(est_nbre_palindrome(214312))
False
print(est_nbre_palindrome(213312))
True


