import re

required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
can_be_ignored = {'cid'}

validation_rules = {
    'byr': lambda x: (len(x) == 4) and ('1920' <= x <= '2002'),
    'iyr': lambda x: (len(x) == 4) and ('2010' <= x <= '2020'),
    'eyr': lambda x: (len(x) == 4) and ('2020' <= x <= '2030'),
    'hgt': lambda x: len(x) == 5 and (x.endswith('cm') and '150cm' <= x <= '193cm') or (x.endswith('in') and '59in' <= x <= '76in'),
    'hcl': lambda x: re.match(r'^#[0-9a-f]{6}$', x),
    'ecl': lambda x: x in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
    'pid': lambda x: re.match(r'^[0-9]{9}$', x),
    'cid': lambda x: True,
}


def validate_passport(passport):
    keys = set(parse_passport(passport).keys())
    diff = required ^ keys

    return not bool(diff) or diff.issubset(can_be_ignored)


def validate_passport_ex(passport):
    return validate_passport(passport) and validate_passport_values(passport)


def parse_passport(passport):
    kvs = {}

    for key in passport.split():
        k, v = key.split(':')
        kvs[k] = v

    return kvs


def validate_passport_values(passport):
    for k, v in parse_passport(passport).items():
        if not validation_rules[k](v):
            return False

    return True


def validate_passports(lines, validator=validate_passport):
    current = []
    valid_count = 0

    for line in [x.strip() for x in lines]:
        if not line:
            valid_count += validator(' '.join(current))
            current = []
            continue

        current.append(line)

    if current:
        valid_count += validator(' '.join(current))

    return valid_count


def test_validate_passports():
    assert 2 == validate_passports(open('input/04.test').readlines())
    assert 0 == validate_passports(open('input/04-2-invalid.test'), validator=validate_passport_ex)
    assert 4 == validate_passports(open('input/04-2-valid.test'), validator=validate_passport_ex)


def test_validation_rules():
    assert not validation_rules['byr']('1919')
    assert not validation_rules['byr']('2003')
    assert not validation_rules['byr']('200')
    assert validation_rules['byr']('1920')
    assert validation_rules['byr']('2002')


if __name__ == '__main__':
    print(validate_passports(open('input/04').readlines()))
    print(validate_passports(open('input/04').readlines(), validator=validate_passport_ex))
