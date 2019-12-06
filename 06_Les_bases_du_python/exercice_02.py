print('Saisissez un nombre :')
nbr = input()
nbr = int(nbr)

result_diviseur = []

for i in range(2, nbr):
    if nbr % i == 0:
        result_diviseur.append(i)

if not result_diviseur:
    print('{} est premier.'.format(nbr))
else:
    print('Les diviseurs de {} sont : '.format(nbr))
    for diviseur in result_diviseur:
        print(' {} '.format(diviseur))
