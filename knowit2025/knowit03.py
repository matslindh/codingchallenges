from common import rs

entries = []

for line in rs('input/03.txt')[1:]:
    navn, snill, slem, pepperkaker = line.split(',')
    score = int(snill) * 25 * 2 - int(slem) * 25 + 15 * int(pepperkaker)

    entries.append((score, navn))

sorted_entries = tuple(sorted(entries))

print(sorted_entries[:3])
print(sorted_entries[-3:])
