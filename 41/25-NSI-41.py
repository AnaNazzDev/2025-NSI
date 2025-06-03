def ou_exclusif(tab1, tab2):
    lenght = len(tab1)
    result = []
    for i in range(lenght):
        e1 = tab1[i]
        e2 = tab2[i]
        if (e1 == 1 and e2 == 1):
            result.append(0)
        elif (e1 == 1 or e2 == 1):
            result.append(1)
        else:
            result.append(0)
    return result

print(ou_exclusif([1, 0, 1, 0, 1, 1, 0, 1], [0, 1, 1, 1, 0, 1, 0, 0]))
# [1, 1, 0, 1, 1, 0, 0, 1]
print(ou_exclusif([1, 1, 0, 1], [0, 0, 1, 1]))
# [1, 1, 1, 0]


class Carre:
    def __init__(self, liste, n): 
        self.ordre = n        
        self.tableau = [[liste[i + j * n] for i in range(n)] 
                        for j in range(n)] 
                                   
    def affiche(self):        
        '''Affiche un carré''' 
        for i in range(self.ordre): 
            print(self.tableau[i]) 
                                   
    def somme_ligne(self, i): 
        '''Calcule la somme des valeurs de la ligne i''' 
        somme = 0             
                                   
        for j in range(self.ordre): 
            somme = somme + self.tableau[i][j] 
        return somme          
                                   
    def somme_col(self, j):   
        '''Calcule la somme des valeurs de la colonne j''' 
        somme = 0
                                   
        for i in range(self.ordre): 
            somme = somme + self.tableau[i][j] 
        return somme          
                                   
                                   
    def est_semimagique(self): 
        s = self.somme_ligne(0) 
        #test de la somme de chaque ligne 
        for i in range(self.ordre): 
            if self.somme_ligne(i) != s: 
                return False
                                   
        #test de la somme de chaque colonne 
        for j in range(self.ordre): 
            if self.somme_col(j) != s: 
                return False
                                   
        return True
    
lst_c3 = [3, 4, 5, 4, 4, 4, 5, 4, 3]
c3 = Carre(lst_c3, 3)
c3.affiche()
# [3, 4, 5]
# [4, 4, 4]
# [5, 4, 3]
c3b = [2, 9, 4,
               7, 0, 3,
               6, 1, 8]

c3b = Carre(c3b, 3)
c3b.affiche()
print(c3b.est_semimagique())


