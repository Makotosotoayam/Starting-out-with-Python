import sys 
print("Work Hours")
clock_in = int(input("Enter the time when you clocking in at work (1-12)\t: "))

if clock_in > 12:
    print("it cannot be over 12 o'clock.")
    sys.exit()

clock_out = int(input("Enter the time when you clocking out of work (1-24)\t: "))

if clock_out < 1:
    print("it cannot be under 1 o'clock")
    sys.exit()

totalhours_ofwork = clock_out - clock_in

if totalhours_ofwork < 0: 
    totalhours_ofwork += 12

print(f"The total hours you work is: {totalhours_ofwork} hours") 