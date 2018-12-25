import bisect


def kind_removesort(f):
    data = [int(i.strip()) for i in f.readlines()]

    sequences = [[]] * len(data)
    best = [9999999999] * len(data)
    print(sequences)

    for i in data:
        best_idx = bisect.bisect_left(best, i)
        best[best_idx] = i
        print(best, best_idx)

        if not sequences[best_idx]:
            sequences[best_idx].append(i)
        elif sequences[best_idx][-1] > i:
            sequences[best_idx][-1] = i

        print(sequences)


# reference
def foo(f):
    X = [int(x) for x in f.read().strip().split('\n')]

    N = len(X)
    P = [0] * N
    M = [0] * (N + 1)
    L = 0
    for i in range(N):
        lo = 1
        hi = L
        while lo <= hi:
            mid = (lo + hi) // 2
            if (X[M[mid]] <= X[i]):
                lo = mid + 1
            else:
                hi = mid - 1

        newL = lo
        P[i] = M[newL - 1]
        M[newL] = i

        if (newL > L):
            L = newL

    S = []
    k = M[L]
    for i in range(L - 1, -1, -1):
        S.append(X[k])
        k = P[k]

    print(S[::-1])
    print(len(S[::-1]))


def test_kind_removesort():
    assert kind_removesort(open('input/07.test')) == 10


if __name__ == '__main__':
    print(foo(open('input/07')))
    print(kind_removesort(open('input/07')))
