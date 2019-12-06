from math import pi

print('Saisissez la hauteur du cone droit : ')
height = input()
print('Saisissez le rayon du cone droit : ')
rayon = input()

volume = (pi * (float(rayon)**2) * float(height)) / 3

print('Le volume du cone droit est {}'.format(volume))
