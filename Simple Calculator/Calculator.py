#Simple Area Calculator

from math import pi
print('1. Square')
print('2. Rectangle')
print('3. Triangle')
print('4. Circle')

choice = int(input('Choose a shape to calculate its area: '))

while choice < 1 or choice > 4:
  choice = int(input('Choice must be between 1-4: '))

if choice == 1:
  side = float(input('What is the side: '))
  while side < 0:
    side = float(input('Side cannot be negative: '))
  area = round(side * side, 2)
  print(f'The area of the square is: {area} cm²')
  
if choice == 2:
  length = float(input('What is the length: '))
  while length < 0:
    length = float(input('Length cannot be negative: '))
  width = float(input('What is the width: '))
  while width < 0:
    width = float(input('Width cannot be negative: '))
  area = round(width * length, 2)
  print(f'The area of the rectangle is: {area} cm²')

if choice == 3:
  base = float(input('What is the base: '))
  while base < 0:
    base = float(input('Base cannot be negative: '))
  height = float(input('What is the height: '))
  while height < 0:
    height = float(input('Height cannot be negative: '))
  area = round((base * height) / 2 , 2)
  print(f'The area of the triangle is: {area} cm²')

if choice == 4:
  radius = float(input('What is the radius: '))
  while radius < 0:
    radius = float(input('Radius cannot be negative: '))
  area = round(pi * radius ** 2 , 2)
  print(f'The area of the circle is: {area} cm²')