def is_marker_found(input: str, length, index: int) -> bool:
    seq = input[index-length:index]
    return len(set(seq)) == len(seq)


def solve_first(input: str) -> int:
    marker_length = 4
    for i in range(marker_length, len(input)):
        if is_marker_found(input, marker_length, i):
            return i
            
    return -1


def solve_second(input: str) -> int:
    marker_length = 14
    for i in range(marker_length, len(input)):
        if is_marker_found(input, marker_length, i):
            return i
            
    return -1


if __name__ == "__main__":
    input_file = "input.txt"
    # input_file = "input_test.txt"
    
    input = []
    with open(input_file, "r") as f:
        input = f.readlines()

    print(f"first: {solve_first(input[0])}")
    print(f"second: {solve_second(input[0])}")
