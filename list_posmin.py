number_list = []
count = int(input('Enter the number of items to identify: '))

for i in range(count):
    number = int(input(f"Enter number {i+1}\t: "))
    number_list.append(number)

positive_numbers = [x for x in number_list if x > 0]
negative_numbers = [x for x in number_list if x < 0]

print('Positive Numbers\t:', positive_numbers)
print('Negative Numbers\t:', negative_numbers)