
census = []


while True:
    try:
        residents = int(input("Enter the number of residents: "))
        if residents > 0:
            break
        else:
            print("The number of residents must be greater than 0.")
    except ValueError:
        print("Invalid input. Please enter an integer.")


for i in range(residents):
    while True:
        try:
            age = float(input(f"Enter the age of resident #{i+1}: "))
            if 0 <= age <= 150: 
                census.append(age)
                break
            else:
                print("Please enter an age between 0 and 150.")
        except ValueError:
            print("Invalid input. Please enter a number.")


total = 0
max1 = max2 = float('-inf')
min1 = min2 = float('inf')

for age in census:
    total += age

    if age > max1:
        max2 = max1
        max1 = age
    elif age > max2:
        max2 = age

    if age < min1:
        min2 = min1
        min1 = age
    elif age < min2:
        min2 = age
        
average_age = total / residents

print(f'''
The average age is            : {average_age:.2f} years
The oldest age 1 is           : {max1} years
The oldest age 2 is           : {max2} years
The youngest age 1 is         : {min1} years
The youngest age 2 is         : {min2} years
''')