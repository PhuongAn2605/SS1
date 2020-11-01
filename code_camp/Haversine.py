from math import *


def main():
    # place1 = [53.4, -3]
    # place2 = [40.71, -74]

    place1 = [28.426846,77.088834]
    place2 = [28.394231,77.050308]
    longtitude = [place1[1], place2[1]]

    lattitude = [place1[0], place2[0]]
    print(radians(place1[0]))
    print(radians(place1[1]))
    haversine(longtitude, lattitude)


def haversine(longtitude, lattitude):
    R = 6371
    delta_long = radians(longtitude[1] - longtitude[0])
    delta_lat = radians(lattitude[1] - lattitude[0])

    x = sin(delta_lat/2)**2 + cos(lattitude[1]) * cos(lattitude[0]) * sin(delta_long/2)**2
    #print(x)
    d = 2 * R * asin(sqrt(x))
    print('{:{width}.{prec}f}'.format(d, width=3, prec=2))


main()