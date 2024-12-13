def alphabet():
    char = str(input("Input the alphabet character\t: ")).upper()

    vowels = str(['A','I','U','E','O'])
    semi_vowels = str(['Y','W'])

    if char in vowels:
         print ("THIS IS A VOWELS")
    elif char in semi_vowels:
        print ("THIS IS A SEMI VOWELS")
    else:
         print ("THIS IS A CONSONANT")
alphabet()                                
