import hashlib
import json


def hash_message(f):
    characters = json.load(f)
    hash = hashlib.md5(b'julekalender').hexdigest()
    s = ''

    while characters:
        drop = None

        for idx, desc in enumerate(characters):
            calculated = hashlib.md5((hash + desc['ch']).encode('iso-8859-1')).hexdigest()
            # print(desc['ch'], calculated, desc['hash'])

            if calculated == desc['hash']:
                s += desc['ch'].encode('iso-8859-1').decode('utf-8')
                drop = idx
                break

        if drop is None:
            print("no drop, exiting")
            return s

        hash = calculated
        del characters[drop]

    return s


def test_hash_message():
    assert hash_message(open('input/09.test')) == 'ubåt'


if __name__ == '__main__':
    print(hash_message(open('input/09')))