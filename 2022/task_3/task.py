def item_to_priority(item: str) -> int:
    result = ord(item)

    if item.islower():
        result = result - ord("a") + 1
    else:
        result = result - ord("A") + 27

    return result


def solve_first(input: list[str]) -> int:
    result = 0

    for line in input:
        line = line.rstrip()

        first_part = line[: len(line) // 2]
        second_part = line[len(line) // 2 :]

        first = set(first_part)
        second = set(second_part)

        common = first.intersection(second)
        for item in common:
            result += item_to_priority(item)

    return result


def solve_second(input: list[str]) -> int:
    result = 0

    group = []
    for line in input:
        line = line.rstrip()

        group.append(line)

        if len(group) != 3:
            continue
            
        first = set(group[0])
        second = set(group[1])
        third = set(group[2])
        
        group = []
        
        common = first.intersection(second)
        common = common.intersection(third)
        for item in common:
            result += item_to_priority(item)

    return result


if __name__ == "__main__":
    input = []
    with open("input_test.txt", "r") as f:
        # with open("input_test.txt", "r") as f:
        input = f.readlines()

    print(f"first: {solve_first(input)}")
    print(f"second: {solve_second(input)}")
