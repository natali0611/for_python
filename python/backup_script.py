#!/usr/bin/env python

import shutil 
 
def backup_dir(src, dst): 
    try: 
        shutil.copytree(src, dst, copy_function=shutil.copy2) 
        print(f"Backup of {src} successful. Files are copied to {dst}") 
    except FileExistsError: 
        print(f"Backup destination {dst} already exists. Please choose a different destination.") 
    except shutil.Error as e: 
        for src, dst, msg in e.args[0]: 
            print(f"Error: {dst}: {msg}") 
 
def main(): 
    source_directory = '/path/to/source_directory' 
    backup_directory = '/path/to/backup_directory' 
 
    backup_directory(source_directory, backup_directory) 
 
if __name__ == "__main__": 
    main() 
 