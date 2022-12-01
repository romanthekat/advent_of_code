def solve_first(input: list[str]):
    max_calories = 0

    calories = 0
    for line in input:
        if line == "\n":
            max_calories = max(calories, max_calories)
            calories = 0
            continue

        calories += int(line)

    return max_calories

def solve_second(input):
    pass


if __name__ == '__main__':
    input = []
    with open("input.txt") as file:
        for line in file:
            input.append(line)

    print(f"first: {solve_first(input)}")
    # print(f"second: {solve_second(input)}")
