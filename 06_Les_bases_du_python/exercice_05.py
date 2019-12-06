def minMaxMoy(list):
    dict = {}
    dict['max'] = max(list)
    dict['min'] = min(list)

    counter = 0
    somme = 0

    for item in list:
        counter += 1
        somme += item

    dict['moy'] = somme/counter
    return dict

list_chiffres = [10,18,14,20,12,16]

results = minMaxMoy(list_chiffres)

print("Le minimum est : {}".format(results['min']))
print("Le maximum est : {}".format(results['max']))
print("La moyenne est : {}".format(results['moy']))
