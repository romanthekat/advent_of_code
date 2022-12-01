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
    elves = []

    calories = 0
    for line in input:
        if line == "\n":
            elves.append(calories)
            calories = 0
            continue

        calories += int(line)
    elves.append(calories)

    elves = sorted(elves, reverse=True)

    return elves[0] + elves[1] + elves[2]

if __name__ == '__main__':
    input = []
    with open("input.txt") as file:
        for line in file:
            input.append(line)

    print(f"first: {solve_first(input)}")
    print(f"second: {solve_second(input)}")
