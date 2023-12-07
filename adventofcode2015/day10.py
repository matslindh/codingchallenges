from itertools import groupby


def look_and_say(s):
    res = ""

    for _, g in groupby(s):
        chars = list(g)
        res += f"{len(chars)}{chars[0]}"

    return res



def test_look_and_say():
    assert look_and_say("1") == "11"
    assert look_and_say("11") == "21"
    assert look_and_say("21") == "1211"
    assert look_and_say("1211") == "111221"
    assert look_and_say("111221") == "312211"


current = "3113322113"

for i in range(50):
    current = look_and_say(current)

print(len(current))