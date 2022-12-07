from typing import List

all_directories = []


class Directory:
    def __init__(self):
        self.directories = {}
        self.files = []
        self.calculated_size = None

    def add_directory(self, directory):
        new_directory = Directory()
        self.directories[directory] = new_directory
        all_directories.append(new_directory)

    def add_file(self, file):
        self.files.append(file)

    def size(self):
        if self.calculated_size is not None:
            return self.calculated_size

        size = 0

        for directory in self.directories.values():
            size += directory.size()

        for file in self.files:
            size += file[1]

        self.calculated_size = size
        return size


def build_tree(lines) -> Directory:
    root = Directory()
    all_directories.append(root)
    stack: List[Directory] = [root]

    for line in lines[1:]:
        current = stack[-1]

        if line.startswith('$ cd '):
            dest = line[5:]

            if dest == '..':
                stack.pop()
            else:
                stack.append(current.directories[dest])
        elif line == '$ ls':
            continue
        elif line.startswith('dir '):
            current.add_directory(line[4:])
        else:
            size, name = line.split(' ')
            current.add_file((name, int(size)))

    return root


def sum_directory_sizes_below(path):
    build_tree(open(path).read().splitlines())
    summed = sum(directory.size() for directory in all_directories if directory.size() <= 100000)
    necessary_to_free = abs(70_000_000 - all_directories[0].size() - 30_000_000)
    space_to_free = None

    for size in sorted([directory.size() for directory in all_directories]):
        if size > necessary_to_free:
            space_to_free = size
            break

    return summed, space_to_free


def test_sum_directory_sizes_below():
    assert sum_directory_sizes_below('input/07.test') == (95437, 24933642)


if __name__ == '__main__':
    print(sum_directory_sizes_below('input/07'))