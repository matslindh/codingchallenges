def fuel_required_for_mass(mass):
    return mass // 3 - 2

def fuel_required_until_limit(mass):
    required_fuel = []
    
    while True:
        fuel_required = fuel_required_for_mass(mass)
        
        if fuel_required <= 0:
            return sum(required_fuel)

        required_fuel.append(fuel_required)
        mass = fuel_required

def sum_file(p):
    with open(p) as f:
        v = [l.strip() for l in f.readlines()]
        return sum([fuel_required_for_mass(int(m)) for m in v]), sum([fuel_required_until_limit(int(m)) for m in v])

def test_fuel_calculator():
    assert fuel_required_for_mass(12) == 2
    assert fuel_required_for_mass(14) == 2
    assert fuel_required_for_mass(1969) == 654
    assert fuel_required_for_mass(100756) == 33583

def test_fuel_limit_calculator():
    assert fuel_required_until_limit(14) == 2
    assert fuel_required_until_limit(1969) == 966
    assert fuel_required_until_limit(100756) == 50346

if __name__ == '__main__':
    print(sum_file('input/01'))
