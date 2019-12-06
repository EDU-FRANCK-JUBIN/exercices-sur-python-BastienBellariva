from math import factorial

e = 2.71828182845904523536

print('Entrez une valeur supérieure à 50 :')
n = input()
n = int(n)

tab=[]
tab.append(0)

for i in range(0, n+1):
    tab[0] = tab[0] + (1/factorial(i))

tab.append(abs(e-tab[0]))

print(tab)

# print("Notre resultat est : {}.".format(tab[0]))
# print("Notre erreur d'approximation est : {}.".format(tab[1]))

