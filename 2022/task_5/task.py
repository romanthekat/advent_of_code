from typing import Tuple

def split_input(input: list[str]) -> list[list[str]]:
    for i, line in enumerate(input):
        if line == "\n":
            return [input[:i], input[i+1:]]
    
    return [[], []]

def parse_crates(input: list[str]) -> list[list[str]]:
   crates_count = len(input[-1]) // 4
   stacks = [[] for _ in range(crates_count)]
   
   input = input[:-1]
   input = input[::-1]
   
   for i in range(crates_count):
       crate_line_index = i*3 + 1 + i
       for height in range(len(input)):
           crate = input[height][crate_line_index]
           if crate == " ":
               break
           stacks[i].append(crate)
   
   return stacks

def parse_command(command: str) -> Tuple[int, int, int]:
    move, crates = command.split(" from ")
    
    move = move.split("move ")[-1]
    crates = crates.split(" to ")
    
    return int(move), int(crates[0]) - 1, int(crates[1]) - 1


def get_result(crates: list[list[str]]) -> str:
    result = ""
    for crate in crates:
        result += crate[-1]
    return result


def solve_first(input: list[str]) -> str:
    crates_input, commands_input = split_input(input) 
    crates = parse_crates(crates_input)
    
    for command in commands_input:
        count, start, end = parse_command(command)
        for _ in range(count):
            crate = crates[start].pop()
            crates[end].append(crate)
    
    return get_result(crates)


def solve_second(input: list[str]) -> str:
    crates_input, commands_input = split_input(input) 
    crates = parse_crates(crates_input)
    
    for command in commands_input:
        count, start, end = parse_command(command)
        
        batch = crates[start][-count:]
        crates[start] = crates[start][:-count]
        for crate in batch:
            crates[end].append(crate)
    
    return get_result(crates)


if __name__ == "__main__":
    input_file = "input.txt"
    # input_file = "input_test.txt"
    
    input = []
    with open(input_file, "r") as f:
        input = f.readlines()

    print(f"first: {solve_first(input)}")
    print(f"second: {solve_second(input)}")
