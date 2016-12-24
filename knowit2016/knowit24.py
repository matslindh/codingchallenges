import string

# this will probably be GODJUL, let's check.
inp = 90101894
letters = ''

while 1:
    l = inp % 26
    letters = string.ascii_uppercase[l-1] + letters

    if inp < 26:
        break

    inp //= 26

print(letters)