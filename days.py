
print('Convert to days')

day_month = 30
day_year = 365

day = int(input('Enter the amount of day/s : '))

year = int(day / day_year)
day = day % day_year

month = int(day / day_month)
day = day % day_month

print (f"The result : {year} year/s {month} month/s {day} day/s")