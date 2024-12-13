print('=' * 99)
print('\tTop 10 Favorite Artists This Year')
print('=' * 99)

artist_list = []
print('Enter the names of your favorite artists one by one:')

while len(artist_list) < 10:
    artist = input(f'Enter the name of artist #{len(artist_list) + 1}\t: ')
    artist_list.append(artist)

print('\nYour Top 10 Favorite Artists This Year:')
print('=' * 40)
for x, artist in enumerate(artist_list, start=1):
    print(f'{x}. {artist}')