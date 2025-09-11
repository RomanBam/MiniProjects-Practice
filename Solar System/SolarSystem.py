from math import pi as pi
from random import choice as ch

planets = [
  'Mercury',
  'Venus',
  'Earth',
  'Mars',
  'Saturn'
]

random_planet = ch(planets)
print(f'{random_planet}\n')

if random_planet == 'Mercury':
  r = 2440
  area = 4 * pi * r **2
  result = round(area,1)
  print(f'The area of Mercury is: {result} km²')

elif random_planet == 'Venus':
  r = 6052
  area = 4 * pi * r **2
  result = round(area,1)
  print(f'The area of Venus is: {result} km²')

elif random_planet == 'Earth':
  r = 6371
  area = 4 * pi * r **2
  result = round(area,1)
  print(f'The area of Earth is: {result} km²')

elif random_planet == 'Mars':
  r = 3390
  area = 4 * pi * r **2
  result = round(area,1)
  print(f'The area of Mars is: {result} km²')

elif random_planet == 'Saturn':
  r = 58232
  area = 4 * pi * r **2
  result = round(area,1)
  print(f'The area of Saturn is: {result} km²')

else:
  print('Oops! An error occured.')