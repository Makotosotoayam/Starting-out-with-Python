total = 0 
for a in range(2,11,2):
     print (a,end= " ")
     total = total + a
     if a < 10:
          print(end= "+ ")
print ("=", total)