import random


def validation(value, authorize_values):
    if not value:
        return False
    else:
        for letter in value:
            if letter not in authorize_values:
                return False
    return True


def generate_chaine(authorize_values, type):
    chaine = ""
    if type == "chaine" :
        counter = 20
    elif type == "sequence":
        counter = 2
    else:
        return False

    for i in range(0, counter):
        chaine += random.choice(authorize_values)

    if validation(chaine, authorize_values):
        return chaine
    else:
        generate_chaine(authorize_values)


def proportion(chaine, sequence):
    print("chaine : {}".format(chaine))
    print("sequence : {}".format(sequence))
    occurence = chaine.count(sequence)
    print("Il y a {proportion} % de \"{sequence}\" dans la chaine ADN.".format(
        proportion=(occurence*100)/(len(chaine)/len(sequence)),
        sequence=sequence
    ))


values_for_chaine = ["a", "t", "g", "c"]

proportion(
    generate_chaine(values_for_chaine, "chaine"),
    generate_chaine(values_for_chaine, "sequence")
)
