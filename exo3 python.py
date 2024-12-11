import os 

def read_to_buffer(filename): 
    with open(filename, 'r') as f:
        return f.read()
    
def read_to_words(filename): 
    with open(filename, 'r') as f:
        return f.read().split()
    
def rename_file(filename): 
    with open(old, new) as f:
        os.rename(old,new)

def find_file_extension(extension, directory):
    files=[]
    for file in os.listdir(directory):
        if file.endswitch(extension):
            files.append(file)
    return files

def display_files(directory):
    for file in os.listdir(directory):
        print(file)

print(read_to_buffer("C:\Users\gasni\Desktop\fich.txt"))
print(read_to_words("C:\Users\gasni\Desktop\fich.txt"))
rename_file("C:\Users\gasni\Desktop\fich.txt")
 