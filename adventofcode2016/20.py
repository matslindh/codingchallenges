intervals = []

def sort_contained_intervals(n):
    n.intervals_start = sorted(n.intervals_start, key=lambda x: x[0])
    n.intervals_end = sorted(n.intervals_end, key=lambda x: x[1])

    if n.left:
        sort_contained_intervals(n.left)

    if n.right:
        sort_contained_intervals(n.right)


class Node:
    def __init__(self, node_start, node_end):
        self.center = node_start + int((node_end - node_start) / 2)
        self.node_start = node_start
        self.node_end = node_end
        self.left = None
        self.right = None
        self.intervals_start = []
        self.intervals_end = []

        #print("Creating tree with start", self.node_start, 'end', self.node_end, 'center', self.center)

    def add(self, start, end):
        if end < self.center:
            if self.left is None:
                #print("new left", self.center)
                self.left = Node(self.node_start, self.center - 1)

            self.left.add(start, end)
        elif start > self.center:
            if self.right is None:
                #print("new right", self.center)
                self.right = Node(self.center + 1, self.node_end)

            self.right.add(start, end)
        else:
            # overlap
            self.intervals_start.append((start, end))
            self.intervals_end.append((start, end))

    def max_end_intersects(self, x):
        m = None

        if x < self.center:
            # find largest end to the left
            if self.left is not None:
                m = self.left.max_end_intersects(x)

            # if we have a interval that ends further back, but starts to the left of x
            # this can be optimized as a binary search
            for i in self.intervals_start:
                if i[0] > x:
                    break

                if not m or i[1] > m:
                    m = i[1]

        elif x > self.center:
            # find largest end to the right
            if self.right is not None:
                m = self.right.max_end_intersects(x)

            if self.intervals_end:
                if x > self.intervals_end[len(self.intervals_end)-1][1]:
                    pass
                elif not m or self.intervals_end[len(self.intervals_end) - 1][1] > m:
                    m = self.intervals_end[len(self.intervals_end)-1][1]
        else:
            # we only need to consider our own intervals, since we're at center
            if self.intervals_end:
                m = self.intervals_end[len(self.intervals_end) - 1][1]

        return m


limit = 4294967295
#limit = 9
#limit = 20
root = Node(0, limit)

print("Building Interval Tree")
for line in open("input/dec20").readlines():
    start, end = line.strip().split('-')

    #print("new interval", start, end)
    root.add(int(start), int(end))
    intervals.append((int(start), int(end)))

print("Sorting start/end intervals")
sort_contained_intervals(root)
idx = 0

print("Searching..")
allowed_count = 0
first_allowed = None

intervals = sorted(intervals, key=lambda x: x[0])


def find_next_interval_start(i):
    # sure we could binary search this
    for start, end in intervals:
        if start > i:
            return start

    return None

while 1:
    m = root.max_end_intersects(idx)

    if not m:
        if not first_allowed:
            first_allowed = idx

        next = find_next_interval_start(idx)

        if next is None:
            print(idx, limit)
            allowed_count += (limit - idx) + 1
            break

        allowed_count += next - idx
        idx = next
    else:
        idx = m+1

print('first allowed', first_allowed, ' total allowed: ', allowed_count)