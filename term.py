print('='*25)
print('Calculating the Term')
print('='*25)

a = int(input('Enter the first term (a)\t: '))
b = int(input('Enter the difference (b)\t: '))
n = int(input('Enter the term number (n)\t: '))

U_n = a + (n - 1) * b

print(f'Term {n}\t: {U_n}')