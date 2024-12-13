numb = int(input('enter a number 1-10 \t: '))

roman = ['I', 'II', 'III','IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']

if 1 <=  numb <= 10:
 print(f"{numb} in roman numerals  : {roman[numb-11]}")
else:
 print("input is wrong")