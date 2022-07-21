class FileSystem:
    def __init__(self):
        self.root = Directory("/")
        
    def create_directory(self, path):
        if FileSystem._validate_path(path):
            folders = path.split("/")
            folders.pop(0)
            roots =[self.root]
                    
            for index, folder in enumerate(folders):
                    if not folder in roots[index].children :
                        new_folder = Directory(folder)
                        roots[index].add_node(new_folder)
                        roots.append(new_folder)
                    else:
                        roots.append(roots[index].children[folder]) 
                        
    def create_file(self, path, contents):
        if FileSystem._validate_path(path):
            folders = path.split("/")
            folders.pop(0)
            roots =[self.root]
            file_name = folders[-1]
            folders.pop(-1)
            if file_name in roots[0].children and len(folders) == 1:
                raise ValueError('')
            
            for index, folder in enumerate(folders):
                    if  folder in roots[index].children :
                        roots.append(roots[index].children[folder]) 
                    else:
                        raise ValueError('')
                        
        
            file =  File(file_name)
            file.write_contents(contents)
            roots[-1].add_node(file)


    def read_file(self, path):
        if FileSystem._validate_path(path):
            folders = path.split("/")
            folders.pop(0)
            roots =[self.root]
            file_name = folders[-1]
            folders.pop(-1)
            
            if file_name in roots[0].children and len(folders) == 1:
                file_obj = roots[0].children[file_name]
                return file_obj.contents
            
            for index, folder in enumerate(folders):
                    if  folder in roots[index].children :
                        roots.append(roots[index].children[folder]) 
                    else:
                        raise ValueError('')
                        
            if file_name in roots[-1].children:
                file_obj = roots[-1].children[file_name]
                return file_obj.contents
            else:
                raise ValueError('')
         
         
    def delete_directory_or_file(self, path):
        if FileSystem._validate_path(path):
            folders = path.split("/")
            folders.pop(0)
            roots =[self.root]
            folder_to_delete =   folders[-1]
            for index, folder in enumerate(folders):
                    if  folder in roots[index].children :                            
                        del_folder = roots[index].children[folder]
                        if folder == folder_to_delete:
                            roots[index].delete_node(folder)
                        roots.append(del_folder)
                    else:
                        raise ValueError('')
        
    def size(self):
        sum = 0
        folders =  self.root.children
        print(folders)
        roots =[self.root]
        for index, child in enumerate(folders):
            if isinstance(folders[child], File):
                sum += len(folders[child].contents)
        return sum


    def __str__(self):
        return f"*** FileSystem ***\n" + self.root.__str__() + "\n***"
    
    @staticmethod
    def _validate_path(path):
        if not path.startswith("/"):
            raise ValueError("Path should start with `/`.")
        return True


    def _find_bottom_node(self, node_names):
        # Write your code here.
        pass


class Node:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name} ({type(self).__name__})"


class Directory(Node):
    
    def __init__(self, name):
        super().__init__(name)
        self.children = {}

    def add_node(self, node):
        self.children[node.name] = node

    def delete_node(self, name):
        del self.children[name]

    def __str__(self):
        string = super().__str__()

        children_strings = []
        for child in list(self.children.values()):
            child_string = child.__str__().rstrip()
            children_strings.append(child_string)

        children_combined_string = indent("\n".join(children_strings), 2)
        string += "\n" + children_combined_string.rstrip()
        return string

class File(Node):
    
    def __init__(self, name):
        super().__init__(name)
        self.contents = ""

    def write_contents(self, contents):
        self.contents = contents

    def __len__(self):
        return len(self.contents)

    def __str__(self):
        return super().__str__() + f" | {len(self)} characters"
    
def indent(string, number_of_spaces):
    spaces = " " * number_of_spaces
    lines = string.split("\n")
    indented_lines = [spaces + line for line in lines]
    return "\n".join(indented_lines)




fs = FileSystem()
fs.create_directory("/dir1")
fs.create_directory("/dir2")
fs.create_directory("/dir1/dir3")
fs.create_file("/dir1/dir3/tim.txt", "Tim is great2!")
fs.create_file("/tim.txt", "Tim is great!")
#fs.delete_directory_or_file("/tim.txt")
print(fs.size())
#with self.assertRaises(ValueError):
#fs.create_directory("/dir3/dir4")
#print(fs)

# fs = FileSystem()

# #with self.assertRaises(ValueError):
# #fs.create_file("/dir1/simon.txt", "ProgrammingExpert is fun!")
# fs.read_file("/tim.txt")
# fs = FileSystem()
# fs.create_file("/tim.txt", "12345")
# fs.size()
# fs.create_file("/alex.txt", "67890")
# fs.size()
# fs = FileSystem()
# fs.create_directory("/dir1")
# fs.create_directory("/dir1/dir2")
# fs.create_directory("/dir1/dir2/dir3")
# fs.create_file("/dir1/dir2/file1.txt", "1")
# fs.create_file("/dir1/dir2/dir3/file2.txt", "1")
# fs = FileSystem()
# #with self.assertRaises(ValueError):
# fs.delete_directory_or_file("/dir1")
# fs.create_directory("/dir1")
# fs.create_file("/dir1/simon.txt", "ProgrammingExpert is fun!")
# #self.assertEqual(25, fs.size())
# #with self.assertRaises(ValueError):
# fs.delete_directory_or_file("/dir2")
# fs.delete_directory_or_file("/dir1")
# fs.size()

