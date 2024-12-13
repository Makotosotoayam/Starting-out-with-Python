def grade():
    student = float(input('enter a student grade (0 out of 100):'))
    
    if student >= 80:
        print('You get an A!')
    elif student >= 70:
        print('You get a B')
    elif student >= 55:
        print('You get a C')
    elif student >= 40:
        print('You get a D')
    elif student >= 1:
        print('You get the lowest score (E)')
grade()       