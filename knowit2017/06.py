from haversine import haversine
from operator import itemgetter
import csv

origin = (59.911491, 10.757933)
places = []
travel_distance = 24 * 7274

with open('input/verda.txt', newline='') as csvfile:
    r = csv.reader(csvfile, delimiter="\t")
    header = None
        
    for row in r:
        if not header:
            header = row
            continue
            
        places.append(dict(zip(header, row)))

capitals = [place for place in places if place['Stadtype bokmål'] == 'Hovedstad']
has_already = {}
unique_capitals = []

for cap in capitals:
    cap['distance'] = haversine(origin, (float(cap['Lat']), float(cap['Lon'])))
    k = str(cap['distance']) + '_' + cap['Stadnamn bokmål']

    if k in has_already:
        continue
        
    unique_capitals.append(cap)
    has_already[k] = True

unique_capitals = sorted(unique_capitals, key=itemgetter('distance')) 

count = 0

for cap in unique_capitals:
    print("Visiting " + cap['Stadnamn bokmål'] + " at distance " + str(cap['distance']) + " " + str(travel_distance) + " to go.")
    travel_distance -= cap['distance'] * 2
    
    if travel_distance < 0:
        print(count)
        break

    count += 1
        
#print(unique_capitals[:3])
