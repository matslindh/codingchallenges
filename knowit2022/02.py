gifts = open("input/02-gaver.txt").read().splitlines()
lines = len(gifts) * 2  # first + last line

for idx, gift in enumerate(gifts[4:], 4):
    lines += 1 if 'alv' in gift else len(gifts) - idx

print(lines)
