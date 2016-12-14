moneys = {}


def add_money(id_, money):
    if id_ not in moneys:
        moneys[id_] = 0

    moneys[id_] += int(money)


def dec_money(id_, money):
    moneys[id_] -= int(money)


for line in open("input/knowit09").readlines():
    inst = line.strip().split(',')

    add_money(inst[1], inst[2])

    if inst[0] != 'None':
        dec_money(inst[0], inst[2])


cnt = 0

for id_ in moneys:
    if moneys[id_] > 10:
        cnt += 1

print(cnt)