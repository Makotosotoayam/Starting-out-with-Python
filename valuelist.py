values = []

number_of_inputs = int(input("Enter the number of inputs: "))

for i in range(number_of_inputs):
    values.append(float(input(f'Value {i+1}: ')))

total = 0
max_value = 0
min_value = values[0]

for value in values:
    total += value 
    if value > max_value:
        max_value = value

    if value < min_value:
        min_value = value

average = total / number_of_inputs

print(f"Largest Value  : {max_value}")
print(f"Smallest Value : {min_value}")
print(f"Average Value  : {average}")