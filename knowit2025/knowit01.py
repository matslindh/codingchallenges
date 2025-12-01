from common import rs

queue = []
password = ''

for line in rs('input/01.txt'):
    if not line.strip():
        continue

    cmd, *obj = line.split(' ', maxsplit=1)

    if cmd == 'ADD':
        queue.append(obj[0])
    elif cmd == 'PROCESS':
        if len(queue) == 0:
            password += 'X'
            continue

        password += queue.pop(0)[0]
    elif cmd == 'COUNT':
        password += str(len(queue))[-1]

print(password)
