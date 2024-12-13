import sys

print("Parking ticket")

enter = int(input("Enter the time you park (6-21) \t : "))
#tempat parkirnya tutup di jam 9 malam
if enter > 21:
    print ("hey you cant park after 21 pm o'clock!") 
    sys.exit()
elif enter < 6:
    print ("you cant park that early!")
    sys.exit()
    
out = int(input("Enter the time you leave the parking lot (7-21) \t : "))
if out < 7:
    print ("it cant be under 7 am o'clock") 
    sys.exit()

total = out - enter

if total <0:
    total += 12

if total <=2:
   park_ticket = 2000
   #Rp.2000 in indonesian
else:
    park_ticket = 2000 + (total - 2) * 500

print(f"Total hours you park : {total} hour")

print (f"Total ticket you must pay : RP {park_ticket}")