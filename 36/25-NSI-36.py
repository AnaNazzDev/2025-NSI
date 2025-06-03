def nombre_de_mots(phrase):
    mots = []
    n = len(phrase)
    temp = ""
    for i in range(n):
        if phrase[i] == " ":
            continue
        if (i < n-1):
            temp += str(phrase[i])
            if (phrase[i+1] == " "):
                mots.append(temp)
                temp = ""
                i += 1
        else:
            if (temp != ""):
                mots.append(temp)
    print("DEBUG", mots)
    return len(mots)

print(nombre_de_mots('Cet exercice est simple.'))
# 4
print(nombre_de_mots('Le point d exclamation est séparé !'))
# 6
print(nombre_de_mots('Combien de mots y a t il dans cette phrase ?'))
# 10
print(nombre_de_mots('Fin.'))
# 1


class Noeud:
    def __init__(self, etiquette):
        '''Méthode constructeur pour la classe Noeud.
        Crée une feuille d'étiquette donnée.'''
        self.etiquette = etiquette
        self.gauche = None
        self.droit = None

    def inserer(self, cle):
        '''Insère la clé dans l'arbre binaire de recherche
        en préservant sa structure.'''
        if cle < self.etiquette:
            if self.gauche != None:
                self.gauche.inserer(cle)
            else:
                self.gauche = Noeud(cle)
        else:
            if self.droit != None:
                self.droit.inserer(cle)
            else:
                self.droit = Noeud(cle)


