songs = {}

# Adding songs to the dictionary with the values as the song name and the key as the artist

# list of english songs by Zayn Malik
songs['Zayn Malik'] = ['Love Yourself', 'Love Me Like You Do', 'Shape of You', 'I See Fire', 'I See Fire']


# list of english songs by Ed Sheeran
songs['Ed Sheeran'] = ['Shape of You', 'I See Fire', 'Castle On The Hill', 'Perfect', 'Galway']


# list of english songs by Anne-Marie
AnneMarie = ['Galway', 'Castle On The Hill', 'Perfect', 'Galway', 'Castle On The Hill']
print(AnneMarie)


# checking zayn malik in the dictionary and printing the songs
if songs['Zayn Malik']:
    print(songs['Zayn Malik'])
    print(songs.get('Zayn Malik'))


# adding Anne-Marie to the dictionary
songs['Anne-Marie'] = AnneMarie
print(songs)   