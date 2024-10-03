print("==================================")
print("Swaping Tripel of x,y,z into y,z,x")
print("==================================")

x = int(input("Input the Value of X : "))
y = int(input("Input the Value of Y : "))
z = int(input("Input the Value of Z : "))

a = x
x = y
y = z
z = a

print(f"The result's is {x},{y},{z}")
