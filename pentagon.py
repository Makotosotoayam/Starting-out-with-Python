print('='*25)
print('Formula of Pentagon')
print('='*25)

def pentagon():
    side = float(input('input the value sides here\t: '))

    area = 1.72 * (side * side)
    perimeter = 5 * side

    print('the resultof the area\t\t: ',round(area))
    print('the result of the perimeter\t: ',round(perimeter))

pentagon()