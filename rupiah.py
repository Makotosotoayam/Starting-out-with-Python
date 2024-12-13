money = int(input("Enter an amount of money in rupiah: RP."))

rp = money

seribu = 1000
b = 500
c = 100
d = 50
e = 25

one = int(money / seribu)
money %= seribu

two = int(money / b)
money %= b

three = int(money / c)
money %= c

four = int(money / d)
money %= d

five = int(money / e)
money %= e

print(f'''
This amount of RP.{rp} is equal as :
     {one}\tpiece RP. {seribu}
     {two}\tpiece RP. {b}
     {three}\tpiece RP. {c}
     {four}\tpiece RP. {d}
     {five}\tpiece RP. {e}
''')