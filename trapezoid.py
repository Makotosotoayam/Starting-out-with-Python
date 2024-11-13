print('='*25)
print('Formula of Trapezoid')
print('='*25)

def trapz():
    a = float(input('enter the roof of trapezoid base value(a)\t: '))
    b = float(input('enter the bottom base of trapezoid value(b)\t: '))
    c = float(input('enter the side value(c)\t: '))
    d = float(input('enter the other side value(d)\t: '))
    h = float(input('enter the height value(h)\t: '))

    area = (a + b) * h / 2
    perimeter = a + b + c + d

    print('the result of the area is\t: ',round(area))
    print('the result of the perimeter is\t: ',round(perimeter))

trapz()