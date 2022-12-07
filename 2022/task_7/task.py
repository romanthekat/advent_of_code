class Dir:
    def __init__(self, name: str, parent) -> None:
        self.name = name
        self.children = {"..": parent}
        self.type = "dir"
        self.size = None
    
    def __str__(self) -> str:
        return "dir " + self.name
    
    def add(self, child):
       self.children[child.get_name()] = child 
    
    def get_size(self):
        if self.size:
            return self.size
        
        size = 0
        
        for name, child in self.children.items():
            # print("object:", self.name, "child:", child)
            if name == "..":
                continue
            size += child.get_size() 
        
        self.size = size
        return size
    
    def get_name(self) -> str:
        return self.name
    
    def get_child(self, name: str):
        return self.children.get(name)
        

class File:
    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size
        self.type = "file"
        
    def __str__(self):
        print(self.size, self.name)
    
    def get_size(self) -> int:
        return self.size
    
    def get_name(self) -> str:
        return self.name
        

def solve_first(input: list[str]) -> int:
    root = Dir("/", None)
    current_folder = root
    
    for line in input[1:]:
        line = line.rstrip()
        print(line)
        if line.startswith("$ cd "):
            target_folder = line.split(" ")[-1]
            current_folder = current_folder.get_child(target_folder) 
        
        elif line.startswith("$ ls"):
            continue
        elif line.startswith("dir "):
            param = line.split(" ")[-1]
            child_folder = current_folder.get_child(param)
            if not child_folder:
                child_folder = Dir(param, current_folder)
                current_folder.add(child_folder)
        else:
            size, filename = line.split(" ")
            file = File(filename, int(size))
            
            current_folder.add(file)
             
    print()
    maximum_size = 100000
    folders = []
    
    folders_to_check = [root]
    while folders_to_check:
        folder = folders_to_check.pop()
        if folder.get_size() <= maximum_size:
            folders.append(folder)
        
        for name, child in folder.children.items():
           if name != ".." and child.type == "dir":
               folders_to_check.append(child)
 
    
    result = 0
    for folder in folders:
        result += folder.get_size()
    
    return result


def solve_second(input: list[str]) -> int:
    return -1


if __name__ == "__main__":
    input_file = "input.txt"
    # input_file = "input_test.txt"
    
    input = []
    with open(input_file, "r") as f:
        input = f.readlines()

    print(f"first: {solve_first(input)}")
    print(f"second: {solve_second(input)}")
