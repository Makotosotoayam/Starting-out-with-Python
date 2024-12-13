print("Converting meter/z")

yard = 0.9144
feet = 0.3048
inch = 0.0254
meter = float(input("enter an amount of meter you want to calculate : "))

yard = int(meter / yard)
feet = int(meter / feet)
inch = int(meter / inch)

print(f"a {meter} meter in a yard is = {yard} yard")
print(f"a {meter} meter in a feet is = {feet} feet")
print(f"a {meter} meter in an inch is = {inch} inch")