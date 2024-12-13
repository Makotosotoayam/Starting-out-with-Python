import sys

print('Approval of a student tests')
print('_'*40)

try:
    letter = input("Enter the Letter grade student: ").upper()
    
    if not letter.isalpha() or len(letter) != 1 or letter not in ['A', 'B', 'C', 'D', 'E']:
        print("Invalid input. Please enter a valid letter grade (A, B, C, D, or E)")
        sys.exit()
    
    math = float(input("Enter the student grade in Math Class (1-100): "))
    
    if math < 1 or math > 100:
            print("Invalid number! Please enter a number between 1 and 100.")
            sys.exit()
    
    ind = float(input("Enter the student grade in Indonesian Class: "))
    
    if ind < 1 or ind > 100:
            print("Invalid number! Please enter a number between 1 and 100.")
            sys.exit()
    
    eng = float(input("Enter the student grade in English Class: "))
    
    if eng < 1 or eng > 100:
            print("Invalid number! Please enter a number between 1 and 100.")
            sys.exit()
    
    hist = float(input('Enter the student grade in History Class: '))
    
    if hist < 1 or hist > 100:
            print("Invalid number! Please enter a number between 1 and 100.")
            sys.exit()
    
    pe = float(input('Enter the student grade in Physical Education: '))
    
    if pe < 1 or pe > 100:
            print("Invalid number! Please enter a number between 1 and 100.")
            sys.exit()
    
    spanis = float(input('Enter the student grade in Spanish: '))
    
    if spanis < 1 or spanis > 100:
            print("Invalid number! Please enter a number between 1 and 100.")
            sys.exit()
    
    scien = float(input('Enter the student grade in Science: '))
    
    if scien < 1 or scien > 100:
            print("Invalid number! Please enter a number between 1 and 100.")
            sys.exit()
    
    art = float(input('Enter the student grade in Art Class: '))
    
    if art < 1 or art > 100:
            print("Invalid number! Please enter a number between 1 and 100.")
            sys.exit()
    
    socdies = float(input('Enter the student grade in Social Studies Class: '))
    
    if socdies < 1 or socdies > 100:
            print("Invalid number! Please enter a number between 1 and 100.")
            sys.exit()
    
    
    if (letter == 'A' or letter == 'B' or letter == 'C') and math >= 60 and ind >= 70 and eng >= 55 and hist >= 75 and pe >= 60 and spanis >= 60 and scien >= 70 and art >= 55 and socdies >= 65:
         print ('''Congratulations! you passed All these test.
         \tʕ •ᴥ•ʔゝ☆''')
    else:
        print('''Oh noooo, you didnt pass one or more the requirements  of these test
        Please contact a teacher to take a remedial to one of these classes
        \tʕ – ᴥ – ʔ''')
except ValueError:
    print('''Heyy, you didnt ejter the right requirements
    \tʕ； •`ᴥ•´ʔ''')
