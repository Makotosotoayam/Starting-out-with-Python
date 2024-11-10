print('='*25)
print('Formula of a Kite')
print('='*25)

def kite():
    length = float(input('Input the lenght here\t: '))
    width = float(input('input the width here\t: '))
    diagonal1 = float(input('input the diagonal_1 here\t: '))
    diagonal2 = float(input('input the diagonal_2 here\t: '))

    perimeter = (diagonal1 * diagonal2) / 2
    area = (2 * length) + (2 * width)

    print("the result of the perimeter\t: ",round(perimeter))
    print("the result of the area is\t: ",round(area))

kite()
print('='*26)
kite()