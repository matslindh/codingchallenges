glows = [6, 2, 5, 5, 4, 4, 6, 3, 7, 6]

low = None
low_point = None

high = None
high_point = None


def ledcount(s):
    lc = 0

    for c in s:
        lc += glows[int(c)]

    return lc


def secondcounts(s):
    leds = 0

    hours, minutes, seconds = hms(s)
    leds += ledcount(str(hours))
    leds += ledcount('{:02d}'.format(minutes))
    leds += ledcount('{:02d}'.format(seconds))

    return leds


def hms(s):
    seconds = s%60
    s -= seconds

    minutes = int(s%3600 / 60)
    s -= minutes * 60

    hours = int(s / 3600)
    return hours, minutes, seconds


for s in range(0, 24*60*60):
    leds = secondcounts(s)

    if not low or leds < low:
        low, low_point = leds, s

    if not high or leds > high:
        high, high_point = leds, s


print(low_point, high_point, hms(high_point - low_point))