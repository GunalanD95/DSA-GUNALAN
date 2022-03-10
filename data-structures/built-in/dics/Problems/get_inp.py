'''
Let us consider a dictionary where longitude and latitude are the keys and the place to which they belong to is the value.

'''

places = {("19.07'53.2", "72.54'51.0"):"Mumbai", \
          ("28.33'34.1", "77.06'16.6"):"Delhi"}


lat = []
long = []
place = []

for i in places:
    lat.append(i[0])
    long.append(i[1])
    place.append(places[i])

print("latitude:", lat)
print("longitude:", long)
print("place:", place)

