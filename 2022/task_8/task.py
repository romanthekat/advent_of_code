def parse_input(input: list[str]) -> list[list[int]]:
    result = []
    
    for line in input:
        line = line.rstrip()
        
        parsed_line = []
        for tree in line:
            parsed_line.append(int(tree))
        
        result.append(parsed_line)
    
    return result


def is_visible(grid: list[list[int]], row, col:int) -> bool:
    height = grid[row][col]
  
    if row == 0 or row == len(grid)-1 or col == 0 or col == len(grid[0])-1:
        return True
    
    for check_row in range(row-1, -1, -1):
        if grid[check_row][col] >= height:
           break 
        
        if check_row == 0:
            return True
    
    for check_row in range(row+1, len(grid)):
        if grid[check_row][col] >= height:
           break 
        
        if check_row == len(grid) - 1:
            return True    
    
    for check_col in range(col-1, -1, -1):
        if grid[row][check_col] >= height:
           break 
        
        if check_col == 0:
            return True
    
    for check_col in range(col+1, len(grid[0])):
        if grid[row][check_col] >= height:
           break 
        
        if check_col == len(grid[0]) - 1:
            return True  

    return False       
   


def solve_first(input: list[str]) -> int:
    grid = parse_input(input)
    
    result = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if is_visible(grid, row, col):
                result += 1
    
    return result
            


def solve_second(input: list[str]) -> int:
    return -1 


    
# 2945 too high
if __name__ == "__main__":
    input_file = "input.txt"
    # input_file = "input_test.txt"

    input = []
    with open(input_file, "r") as f:
        input = f.readlines()

    print(f"first: {solve_first(input)}")
    print(f"second: {solve_second(input)}")
