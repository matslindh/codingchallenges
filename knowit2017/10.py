keep = list(range(1, 1501))
remove = False

while(len(keep) > 1):
    n_keep = []
    
    for person in keep:
        if not remove:
            n_keep.append(person)
            
        remove = not remove

    keep = n_keep

print(keep)
