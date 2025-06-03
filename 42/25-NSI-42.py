def nb_repetitions(element, list):
    count = 0
    for e in list:
        if e == element:
            count += 1
    return count


print(nb_repetitions(5, [2, 5, 3, 5, 6, 9, 5]))
# 3
print(nb_repetitions('A', ['B', 'A', 'B', 'A', 'R']))
# 2
print(nb_repetitions(12, [1, '!', 7, 21, 36, 44]))
# 0

def binaire(a):
    '''convertit un nombre entier a en sa representation 
    binaire sous forme de chaine de caractères.'''
    if a == 0:
        return '0'
    bin_a = ''
    while a > 0: 
        bin_a = str(a % 2) + bin_a
        a = a // 2
    return bin_a

print(binaire(0))
# '0'
print(binaire(77))
# '1001101'


