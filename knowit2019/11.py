def length_of_landing(speed, landing_strip):
    up_mountain = True
    distance = 0
    ice_slide = 1

    for c in landing_strip:
        distance += 1

        if c == 'G':
            speed -= 27
        elif c == 'A':
            speed -= 59
        elif c == 'S':
            speed -= 212
        elif c == 'I':
            speed += 12 * ice_slide
            ice_slide += 1
        elif c == 'F':
            if up_mountain:
                speed -= 70
                up_mountain = False
            else:
                speed += 35
                up_mountain = True

        if c != 'I':
            ice_slide = 1

        if speed <= 0:
            return distance


def test_length_of_landing():
    assert 11 == length_of_landing(300, 'IIGGFFAIISGIFFSGFFAAASS')


if __name__ == '__main__':
    print(length_of_landing(10703437, open('input/11').read().strip()))