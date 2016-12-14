from collections import Counter

cnts = None

for line in open("input/dec06").readlines():
    line = line.strip()

    if not cnts:
        cnts = [Counter() for _ in line]

    for idx in range(0, len(line)):
        cnts[idx].update(line[idx])

password = ''

for cnt in cnts:
    password += cnt.most_common()[-1][0]

print(password)