class Dir:
    def __init__(self, name: str, parent) -> None:
        self.name = name
        self.children = {"..": parent}
        self.type = "dir"
        self.size = None

    def add(self, child):
       self.children[child.get_name()] = child 
    
    def get_size(self):
        if self.size:
            return self.size
        
        size = 0
        for name, child in self.children.items():
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

    def get_size(self) -> int:
        return self.size
    
    def get_name(self) -> str:
        return self.name

        
def parse_commands(input: list[str]) -> Dir:
    root = Dir("/", None)
    current_folder = root
    
    for line in input[1:]:
        line = line.rstrip()
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
    
    return root


def solve_first(input: list[str]) -> int:
    root = parse_commands(input)
             
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
    root = parse_commands(input)
    
    total_size = 70000000
    need_at_least = 30000000
    
    free = total_size - root.get_size()
    delete_at_least = need_at_least - free
    
    folder_to_delete = root
    folders_to_check = [root]
    while folders_to_check:
        folder = folders_to_check.pop()
        size = folder.get_size()
        if size >= delete_at_least and size <= folder_to_delete.get_size():
            folder_to_delete = folder
        
        for name, child in folder.children.items():
            if name != ".." and child.type == "dir":
                folders_to_check.append(child)
            
    
    return folder_to_delete.get_size()


if __name__ == "__main__":
    input_file = "input.txt"
    # input_file = "input_test.txt"
    
    input = []
    with open(input_file, "r") as f:
        input = f.readlines()

    print(f"first: {solve_first(input)}")
    print(f"second: {solve_second(input)}")