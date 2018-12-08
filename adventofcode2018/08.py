def treer(f):
    input = [int(x) for x in f.read().strip().split(' ')]

    def noder(struct, idx):
        childs = struct[idx]
        metadata = struct[idx+1]
        idx += 2
        meta_entries = 0
        child_values = []
        value = 0

        for x in range(0, childs):
            idx, meta_read, child_value = noder(struct, idx)
            meta_entries += meta_read
            child_values.append(child_value)

        metadata_elements = struct[idx:idx+metadata]

        for e in metadata_elements:
            if e - 1 < len(child_values):
                value += child_values[e-1]

            if not childs:
                value += e

            meta_entries += e

        idx += metadata
        return idx, meta_entries, value

    return noder(input, 0)


def test_treer():
    test = treer(open('input/08.test'))

    assert test[1] == 138
    assert test[2] == 66


if __name__ == '__main__':
    print(treer(open('input/08')))