print("="*25)
print("Calculating A Cuboid")
print("="*25)

p = float(input("input the length\t: "))
l = float(input("input the width\t: "))
t = float(input("input the height\t: "))

surface = 2 * (p * l) + (p * t) + (l * t)
volume = p * l * t
area = 4 * (p + l + t)

print("the result of surface\t: ",round(surface))
print("the result of volume\t: ",round(volume))
print("the result of area\t: ",round(area))


