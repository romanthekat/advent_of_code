def solve_first(input: str) -> int:
    for i in range(4, len(input)):
        seq = input[i-4:i]
        if len(set(seq)) == len(seq):
            return i         
            
    return -1


def solve_second(input: str) -> int:
    return -1


if __name__ == "__main__":
    input_file = "input.txt"
    # input_file = "input_test.txt"
    
    input = []
    with open(input_file, "r") as f:
        input = f.readlines()

    print(f"first: {solve_first(input[0])}")
    print(f"second: {solve_second(input[0])}")
