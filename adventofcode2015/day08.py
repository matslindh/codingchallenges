import codecs

def decode(s):
    return codecs.escape_decode(bytes(s, "iso-8859-1"))[0].decode("iso-8859-1")

def escape(s):
    return '"' + s.replace("\\", r"\\").replace("\"", r"\"") + '"'


def test_escape():
    assert escape('""') == r'"\"\""'
    assert escape('"abc"') == r'"\"abc\""'
    assert escape(r'"aaa\"aaa"') == r'"\"aaa\\\"aaa\""'
    assert escape(r'"\x27"') == r'"\"\\x27\""'

if __name__ == '__main__':
    s = 0
    s_escaped = 0

    for line in open("input/08").read().splitlines():
        s += len(line)
        s -= len(decode(line[1:-1]))
        s_escaped += len(escape(line)) - len(line)

    print(s)
    print(s_escaped)