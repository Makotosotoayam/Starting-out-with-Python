import sys
try:
    shoe = int(input("Enter your shoe size (EU Standard) : "))
    if shoe < 36 or shoe > 46:
        print('Sorry, we use the EU standard which is between 36 - 46')
        sys.exit()
    
    elif 40 < shoe <= 46:
         print("Big size")
    elif 36 <= shoe <= 40:
         print("Standard size")
except ValueError:
    print('Sorry, you didn\'t enter the right requirements.')       