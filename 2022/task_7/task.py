class Dir:
    def __init__(self, name: str, parent) -> None:
        self.name = name
        self.size = None
        self.children = {"..": parent}

    def get_name(self) -> str:
        return self.name

    def get_size(self):
        if self.size:
            return self.size

        size = 0
        for name, child in self.children.items():
            if name == "..":
                continue
            size += child.get_size()

        self.size = size
        return size

    def add(self, child):
        self.children[child.get_name()] = child

    def get_child(self, name: str):
        return self.children.get(name)


class File:
    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size

    def get_name(self) -> str:
        return self.name

    def get_size(self) -> int:
        return self.size


def parse_commands(input: list[str]) -> Dir:
    root = Dir("/", None)
    current_dir = root

    for line in input[1:]:
        line = line.rstrip()
        if line.startswith("$ cd "):
            target_dir_name = line.split(" ")[-1]
            current_dir = current_dir.get_child(target_dir_name)

        elif line.startswith("$ ls"):
            continue

        elif line.startswith("dir "):
            dir_name = line.split(" ")[-1]
            child_dir = current_dir.get_child(dir_name)
            if not child_dir:
                child_dir = Dir(dir_name, current_dir)
                current_dir.add(child_dir)

        else:
            size, filename = line.split(" ")
            current_dir.add(File(filename, int(size)))

    return root


def solve_first(input: list[str]) -> int:
    root = parse_commands(input)

    dirs = []
    dirs_to_check = [root]
    while dirs_to_check:
        dir = dirs_to_check.pop()
        if dir.get_size() <= 100000:
            dirs.append(dir)

        for name, child in dir.children.items():
            if name != ".." and isinstance(child, Dir):
                dirs_to_check.append(child)

    return sum(f.get_size() for f in dirs)


def solve_second(input: list[str]) -> int:
    root = parse_commands(input)

    free = 70000000 - root.get_size()
    delete_at_least = 30000000 - free

    dir_to_delete = root
    dirss_to_check = [root]
    while dirss_to_check:
        dir = dirss_to_check.pop()
        size = dir.get_size()
        if size >= delete_at_least and size <= dir_to_delete.get_size():
            dir_to_delete = dir

        for name, child in dir.children.items():
            if name != ".." and isinstance(child, Dir):
                dirss_to_check.append(child)

    return dir_to_delete.get_size()


if __name__ == "__main__":
    input_file = "input.txt"
    # input_file = "input_test.txt"

    input = []
    with open(input_file, "r") as f:
        input = f.readlines()

    print(f"first: {solve_first(input)}")
    print(f"second: {solve_second(input)}")
