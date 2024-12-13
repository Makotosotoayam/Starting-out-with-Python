month = ['January','February','March','April','May','June','July','August','September','October','November','Desember']


print(month[2],month[9])

month[7] = 'August'
month[0] = 'January'

month.append ('Muharram')

for numb,y in enumerate(month):
     
     print(f'Month of the-{numb+1} {y}')
