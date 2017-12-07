import string


def decrypt(word):
    table = {}

    for i, letter in enumerate(string.ascii_uppercase):
        translated = string.ascii_uppercase[((66 + i) * 3 - 2) % len(string.ascii_uppercase)]
        table[translated] = letter

    return ''.join([table[letter] for letter in word])


def test_decrypt():
    assert decrypt('PWVAYOBB') == 'JULEMANN'


if __name__ == "__main__":
    print(decrypt('OTUJNMQTYOQOVVNEOXQVAOXJEYA'))
