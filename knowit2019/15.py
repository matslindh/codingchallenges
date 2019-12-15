import math

def length_of_side(from_x, from_y, from_z, x, y, z):
    return math.sqrt(pow(from_x - x, 2) + pow(from_y - y, 2) + pow(from_z - z, 2))


def length_of_side_points(p1, p2):
    return length_of_side(p1[0], p1[1], p1[2], p2[0], p2[1], p2[2])


def permiter_of_triangle(tri):
    return  length_of_side_points(tri[0], tri[1]) + \
            length_of_side_points(tri[1], tri[2]) + \
            length_of_side_points(tri[2], tri[0])


def area_of_triangle(tri):
    p_2 = permiter_of_triangle(tri) / 2

    return math.sqrt(p_2 * \
        (p_2 - length_of_side_points(tri[0], tri[1])) * \
        (p_2 - length_of_side_points(tri[1], tri[2])) * \
        (p_2 - length_of_side_points(tri[2], tri[0])))


def area_of_model(model):
    area = 0

    for tri in model:
        area += area_of_triangle(tri)

    return area


def volume_of_model(model):
    vol_sum = 0

    for tri in model:
        vol_sum += volume_of_triangle(tri)
        
    return abs(vol_sum)
    

# Based on https://stackoverflow.com/a/1568551/137650    
def volume_of_triangle(tri):
    v321 = tri[2][0] * tri[1][1] * tri[0][2]
    v231 = tri[1][0] * tri[2][1] * tri[0][2]
    v312 = tri[2][0] * tri[0][1] * tri[1][2]
    v132 = tri[0][0] * tri[2][1] * tri[1][2]
    v213 = tri[1][0] * tri[0][1] * tri[2][2]
    v123 = tri[0][0] * tri[1][1] * tri[2][2]

    return (1.0 / 6.0) * (-v321 + v231 + v312 - v132 - v213 + v123)

    
def test_length_of_side():
    assert 10 == length_of_side(0, 0, 0, 10, 0, 0)
    assert 14.142 == round(length_of_side(10, 0, 0, 0, 0, 10), 3)
    assert 10 == length_of_side(0, 0, 10, 0, 0, 0)


def test_length_of_side_points():
    assert 10 == length_of_side_points((0, 0, 0), (10, 0, 0))
    assert 14.142 == round(length_of_side_points((10, 0, 0), (0, 0, 10)), 3)
    assert 10 == length_of_side_points((0, 0, 10), (0, 0, 0))


def test_permiter_of_triangle():
    assert 34.142 == round(permiter_of_triangle(((0, 0, 0), (10, 0, 0), (0, 0, 10))), 3)


def test_area_of_triangle():
    assert 50 == area_of_triangle(((0, 0, 0), (10, 0, 0), (0, 0, 10)))


def test_volume_of_model():
    assert 0.167 == round(volume_of_model(
        (
            ((0,0,0),(10,0,0),(0,0,10)),
            ((0,0,0),(0,0,10),(0,10,0)),
            ((0,0,0),(0,10,0),(10,0,0)),
            ((10,0,0),(0,10,0),(0,0,10)),
        )
    ) / 1000, 3)


if __name__ == '__main__':
    model = []
    
    for row in open('input/model.csv').readlines():
        tri = [float(x) for x in row.strip().split(',')]
        model.append(((tri[0], tri[1], tri[2]), (tri[3], tri[4], tri[5]), (tri[6], tri[7], tri[8])))

    print(round(volume_of_model(model) / 1000, 3))
