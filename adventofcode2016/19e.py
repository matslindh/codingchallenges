import math

data = []
inp = 3004953

for i in range(0, inp):
    data.append(i+1)

idx = 0

while len(data) > 1:
    dst = (idx + math.floor(len(data) / 2)) % len(data)
    del (data[dst])

    if dst > idx:
        idx = (idx + 1) % len(data)

    if len(data) % 1000 == 0:
        print(len(data))

print(data)