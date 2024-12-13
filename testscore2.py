import sys
print("*"*50)
print("Test Score.. again")
print("*"*50)
try:
    score = float(input("Enter a student score : "))
    
    if score < 1 or score > 100 :
            print("Invalid score! Please enter a number between 1 and 100.")
            sys.exit()
    
    if score >= 90 and score <= 100:
         print ('''You get an [A]!
         \tYou did Amazingly
         \t(≧∇≦)/''')
    elif score >= 80:
         print ('''You get a [B]!
         \tYou did the best you can!
         \t(≡^∇^≡)''')
    elif score >= 70:
         print ('''You get a [C]!
         You did incredible! don't let people tell you otherwise
         \t˙˚ʚ(´◡`)ɞ˚˙''')
    elif score >= 60:
         print ('''You get a [D]!
         \tRemember,your score isnt everything
         \t≧﹏≦''')
    elif score <60:
         print ('''You get an [E]!
         \tit's important to remember that one result does not define your potential in the future so just keep learning as much as you can! dont let people bring you down.
         \t❀(*´▽`*)❀''')
except ValueError:
     print ('''hey, you didnt enter the right integer.
     \t凸( •̀_•́ )凸''')
     sys.exit()