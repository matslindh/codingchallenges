import re

def has_abba(s):
    for i in range(0, len(s) - 3):
        if s[i] == s[i+3] and s[i+1] == s[i+2] and s[i] != s[i+1]:
            return True

    return False

cnt = 0

for line in open("input/dec07").readlines():
    segments = re.split(r'[\[\]]', line.strip())
    hypernet = False
    valid = False

    for segment in segments:
        v = has_abba(segment)

        if not hypernet and v:
            valid = True
        elif hypernet and v:
            valid = False
            break

        hypernet = not hypernet

    if valid:
        cnt += 1

print(cnt)