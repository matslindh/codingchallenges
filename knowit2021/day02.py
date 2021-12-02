import csv
from haversine import haversine as haversine2
from math import radians, cos, sin, asin, sqrt


def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance in kilometers between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371  # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
    return c * r


header = True
cities = {}
highest_lat = 0


with open('input/02', encoding='utf-8') as file:
    csv = csv.reader(file)

    for row in csv:
        if header:
            header = False
            continue

        pre, post = row[1].split(' ')
        city = row[0]

        lon = float(pre[6:])
        lat = float(post[:-1])

        cities[city] = (lat, lon)


print(len(cities))

current = (90.0, 0.0)
distance = 0
fr = 'North pole'

while cities:
    dist = None
    best = None
    best_coord = None

    for city, coord in cities.items():
        # meters = sqrt(pow(current[1] - coord[1], 2) + pow(current[0] - coord[0], 2))
        meters = haversine(current[1], current[0], coord[1], coord[0])
        # meters = haversine2(current, coord)

        if not dist or meters < dist:
            dist = meters
            best = city
            best_coord = coord

    distance += dist
    current = best_coord
    del cities[best]
    # print(f"{best_coord[0]},{best_coord[1]},marker,#ff0000,test")
    print(f"travel: {fr} to {best} {best_coord} {dist}")
    fr = best

distance += haversine(current[1], current[0], 0.0, 90.0)
#distance += haversine2(current, (90, 0))
print(distance, round(distance))
