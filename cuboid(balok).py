print("="*25)
print("Calculating A Cuboid")
print("="*25)

p = float(input("input the length\t: "))
l = float(input("input the width\t: "))
t = float(input("input the height\t: "))

surface = lambda p,l,t: 2 * (p * l) + (p * t) + (l * t)
volume = lambda p,l,t: (p * l * t)
area = lambda p,l,t: 4 * (p + l + t)

print(f"LUAS\t\t: {surface(p,l,t)} cm2")
print(f"VOLUME\t\t: {volume(p,l,t)} cm2")
print(f"AREA\t: {area(p,l,t)} cm2")


