
print('Converting to seconds')


sec_minut = 60
sec_hours = 60 * 60
sec_days = 60 * 60 * 24

sec = int(input('Enter the amount of seconds : '))

day = int(sec / sec_days)
sec = sec % sec_days

hour = int(sec / sec_hours)
sec = sec % sec_hours

minute = int(sec / sec_minut)
sec = sec % sec_minut

print(f'The result : {day} day {hour} hour {minute} minute {sec} second')