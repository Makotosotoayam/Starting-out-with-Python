numbers = []
total = 0
average = 0

count = int(input("Enter the number of inputs you want: "))

for i in range(count):
    numbers.append(int(input("Enter a value: ")))

for value in numbers:
    total += value
    average = total / count

print("The total sum is: ", total)
print("The average value is: ", average)