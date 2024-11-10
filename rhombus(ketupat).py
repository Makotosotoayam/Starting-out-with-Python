print('='*25)
print('Formula of a belah ketupat or rhombus')
print('='*25)

def rhombus():
    side = float(input('input the side here: '))
    diagonal1 = float(input('input the diagonal1: '))
    diagonal2 = float(input('input the diagonal2: '))

    perimeter = 4 * side
    area = (diagonal1 * diagonal2) * 0.5

    print('the result of the perimeter\t\t: ',round(perimeter))
    print('the result of the area\t: ',round(area))

rhombus()