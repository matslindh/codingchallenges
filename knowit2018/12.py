input = "😡😚😀😷😨😥😮😀😩😀😤😩😥😌😀😩😀😷😡😮😮😡😀😤😩😥😀😬😩😫😥😀😣😡😥😳😡😲😎😀😱😚😀😨😯😷😀😣😯😭😥😟😀😡😚😀😨😥😀😤😩😥😤😀😡😭😯😮😧😀😨😩😳😀😦😲😩😥😮😤😳😎"
m = ord(min(input))
print(m)

for x in range(0, 127):
    for c in input:
        v = chr(ord(c) - m + x)
        print(v, end='')

    print()
