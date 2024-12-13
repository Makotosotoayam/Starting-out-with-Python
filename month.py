import sys
print("_"*50)
print("returning a month by entering a number 1 to 12")
print("_"*50)
try:
    month =  int(input("enter a number between 1 to 12 : "))

    if month < 1 or month > 12:
        print("Invalid number! Please enter a number between 1 and 12.")
        sys.exit()
        
    if month == 1 :
        print ('Its January')
    elif month == 2 :
        print ('Its February')
    elif month == 3 :
        print ('Its March')
    elif month == 4 :
        print ('Its April')
    elif month == 5 :
        print ('Its May')
    elif month == 6 :
        print ('Its June')
    elif month == 7 :
        print ('Its July')
    elif month == 8 :
        print ('Its August')
    elif month == 9 :
        print ('Its September')
    elif month == 10 :
        print ('Its October')
    elif month == 11 :
        print ('Its November')
    elif month == 12 :
        print ('Its Desember')
except ValueError:
    print("Invalid input! Please enter a valid integer.")
    sys.exit() 