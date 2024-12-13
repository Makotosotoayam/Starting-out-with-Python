grade = int(input("Enter a student test score : "))

if grade >= 75 and grade <= 100:
     print ('''You passed the test!\r
    \tCongratss you made it''')
elif grade <=75:
     print ('''You didnt passed the test :(\r
     \tyou will make it next time!''')
else:
     print ('''you enter the wrong score!\r
     \tThe limit is 100 and start from 0''')