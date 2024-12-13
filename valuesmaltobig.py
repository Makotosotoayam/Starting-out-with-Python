value = [ ]

inputt = int(input("Enter the value: "))

for i in range(inputt):
     value.append(float(input(f'value of-{i+1} : ')))

total = max = 0
min = value[0]

for data in value:
     total += data
     
     if data > max:
          max = data

     if data < min:
          min = data

av = total / inputt
#average = rata2

print(f"Biggest Grade  : {max}")
print(f"Smallest Value : {min}")
print(f"Average Value : {av}")