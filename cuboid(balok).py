print("="*25)
print("Calculating A Cuboid")
print("="*25)

p = float(input("input the length\t: "))
l = float(input("input the width\t: "))
t = float(input("input the height\t: "))

surface_a = 2 * (p * l) + (p * t) + (l * t)
lateral_surface = (2 * t) * (l * w)
volume = p * l * t
perimeter = 4 * (p + l + t)

print("the result of surface area\t: ",round(surface_a))
print("the result of lateral lateral surface\t: ",round(lateral_surface))
print("the result of volume\t\t: ",round(volume))
print("the result of perimeter\t\t: ",round(perimeter))


