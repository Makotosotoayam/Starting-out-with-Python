print('='*25)
print('Calculating the Arithmetic Sequence')
print('='*25)

a = int(input('Enter the first term (a)\t: '))
b = int(input('Enter the common difference (b)\t: '))
n = int(input('Enter the number of terms (n)\t: '))

S_n = int(n / 2) * (2 * a + (n - 1) * b)

print('Sum of the arithmetic sequence : ', S_n)