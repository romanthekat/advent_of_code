def solve_first(input: list[str])-> int:
    result = 0
    response2common = {"X": "A", "Y": "B", "Z": "C"}
    play2score = {"A": 1, "B": 2, "C": 3}
    play2win = {"B": "A", "C": "B", "A": "C"}
    
    for line in input:
        opp = line[0]
        me = response2common[line[2]]
        
        result += play2score[me]
        
        if opp == me:
            result += 3
        elif play2win[me] == opp:
            result += 6
        else:
            pass

    return result

def solve_second(input: list[str])-> int:
    return 0


if __name__ == '__main__':
    input = []
    with open("input.txt", 'r') as f:
        input = f.readlines()

    print(f"first: {solve_first(input)}")
    print(f"second: {solve_second(input)}")

