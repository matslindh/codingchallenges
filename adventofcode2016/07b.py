import re


def abas_babs(s):
    for i in range(0, len(s) - 2):
        if s[i] == s[i+2] and s[i] != s[i+1]:
            yield s[i:i+3], s[i+1] + s[i] + s[i+1]

    return

cnt = 0

for line in open("input/dec07").readlines():
    segments = re.split(r'[\[\]]', line.strip())
    hypernet = False
    valid = False

    for sidx in range(0, len(segments), 2):
        for abas, babs in abas_babs(segments[sidx]):
            for hidx in range(1, len(segments), 2):
                if babs in segments[hidx]:
                    valid = True
                    break

    if valid:
        cnt += 1

print(cnt)
