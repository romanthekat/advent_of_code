def solve_first(input: list[str]) -> int:
    result = 0

    for line in input:
        line = line.rstrip()
        
        parts = line.split(",")
        
        pair1 =[int(n) for n in parts[0].split("-")]
        pair2 = [int(n) for n in parts[1].split("-")]
        
        if (pair1[0] >= pair2[0] and pair1[1] <= pair2[1]) or (pair2[0] >= pair1[0] and pair2[1] <= pair1[1]):
            result += 1

    return result


def solve_second(input: list[str]) -> int:
    result = 0

    for line in input:
        line = line.rstrip()
        
        parts = line.split(",")
        
        pair1 =[int(n) for n in parts[0].split("-")]
        pair2 = [int(n) for n in parts[1].split("-")]
        
        if (pair1[0] <= pair2[0] <= pair1[1]) or (pair2[0] <= pair1[0] <= pair2[1]):
            result += 1

    return result


if __name__ == "__main__":
    input_file = "input.txt"
    # input_file = "input_test.txt"
    
    input = []
    with open(input_file, "r") as f:
        input = f.readlines()

    print(f"first: {solve_first(input)}")
    print(f"second: {solve_second(input)}")
