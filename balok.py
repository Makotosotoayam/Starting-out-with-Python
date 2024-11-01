print("="*20)
print("balok")
print("="*20)

p = int(input("nilai panjang\t: "))
l = int(input("nilai lebar\t: "))
t = int(input("nilai tinggi\t: "))

luas = lambda p,l,t: 2 * (p * l) + (p * t) + (l * t)
volume = lambda p,l,t: (p * l * t)
keliling = lambda p,l,t: 4 * (p + l + t)

print(f"LUAS\t\t: {luas(p,l,t)} cm2")
print(f"VULUME\t\t: {volume(p,l,t)} cm2")
print(f"KELILING\t: {keliling(p,l,t)} cm2")


