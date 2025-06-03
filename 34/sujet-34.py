def tri_selection(tab):
    n = len(tab)
    for i in range(n - 1):
        indice_min = i
        for j in range(i + 1, n):
            if tab[j] < tab[indice_min]:
                indice_min = j
        if indice_min != i:
            temp = tab[i]
            tab[i] = tab[indice_min]
            tab[indice_min] = temp

tab = [1, 52, 6, -9, 12]
tri_selection(tab)
print(tab)  # Affichera : [-9, 1, 6, 12, 52]


from random import randint

def plus_ou_moins():
    nb_mystere = randint(1, 99) 
    nb_test = int(input("Proposez un nombre entre 1 et 99 : "))
    compteur = ... 

    while nb_mystere != nb_test and compteur < 5: 
        compteur = compteur + 1
        if nb_mystere < nb_test: 
            nb_test = int(input("Trop petit ! Testez encore : "))
        else:
            nb_test = int(input("Trop grand ! Testez encore : "))

    if nb_mystere == nb_test:
        print("Bravo ! Le nombre était ", ...) 
        print("Nombre d'essais: ", ...) 
    else:
        print ("Perdu ! Le nombre était ", ...) 

