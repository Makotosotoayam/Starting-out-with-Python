print('='*25)
print('Formula of Hexagon or segi enam')
print('='*25)

def hexagon():
    import math

    side = float(input('input the value sides : '))

    perimeter = 6 * side
    area = (3 * math.sqrt(3) * (side ** 2)) / 2

    print('the result of the perimeter is\t: ',round(perimeter))
    print('the result of the area is\t: ',round(area))

hexagon()