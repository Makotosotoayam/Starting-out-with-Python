import sys
print('+'*25)
print('A Simple Calculator')
print('-'*25)

a1 = float(input('Enter the first number\t:'))


option = input('choose an operator( + - * /) \t: ')

if option not in ['+', '-', '*', '/']:
    print("Invalid operator! Please choose one of (+, -, *, /).")
    sys.exit()

a2 = float(input('Enter the second number\t: '))



plus = a1 + a2
min = a1 - a2
times = a1 * a2
div = a1 / a2

if option == '+':
    print('Result :\t' + str(plus))

elif option == '-':
    print('Result :\t' + str(min))

elif option == '*':
    print('Result :\t' + str(times))

elif option == '/':
    print('Result :\t' + str(div))
else:
    print('ERROR please try again..')
    sys.exit()
    
print('thank you') 