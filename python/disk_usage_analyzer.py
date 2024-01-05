#!/usr/bin/env python
'''Reports the disk usage of each subdirectory within a given directory.
Print a report of the total size of each subdirectory and the top 5 largest files in the entire directory tree.'''
import os 

#calculate size of directory
def get_directory_size(path): 
    total_size = 0 
    for dirpath, dirnames, filenames in os.walk(path): 
        for filename in filenames: 
            filepath = os.path.join(dirpath, filename) 
            total_size += os.path.getsize(filepath) 
    return total_size 
 
#size of five lagest files
def get_largest_files(path, n=5): 
    files_info = [] 
    for dirpath, dirnames, filenames in os.walk(path): 
        for filename in filenames: 
            filepath = os.path.join(dirpath, filename) 
            files_info.append((filepath, os.path.getsize(filepath))) 
    files_info.sort(key=lambda x: x[1], reverse=True) 
    return files_info[:n] 
 

def main(): 
    root_directory = '/home/natali/for_python/git/lesson_2' 
 
    for dirpath, dirnames, filenames in os.walk(root_directory): 
        print(f"Directory: {dirpath}") 
        total_size = get_directory_size(dirpath) 
        print(f"Total size: {total_size} bytes") 
        largest_files = get_largest_files(dirpath) 
        print("Largest files:") 
        for file, size in largest_files: 
            print(f"{file} - {size} bytes") 
        print("\n") 
 
if __name__ == "__main__": 
    main() 
 