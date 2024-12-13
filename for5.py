total = 0
for a in range(1,6):
     print(a, end=" ") 
     total += a 
     if a < 5:
          print(end="+ ")
print("=", total)