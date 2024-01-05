#!/usr/bin/env python
'''Script that backs up files from one directory into another, preserving the directory structure and file metadata.'''
import shutil 
 
source_directory = '/home/natali/for_python/git/lesson_2/dir1' 
backup_directory = '/home/natali/for_python/git/lesson_2/dir2' 
 
shutil.copytree(source_directory, backup_directory, copy_function=shutil.copy2) 
print(f"Backup of {source_directory} successful. Files are copied to {backup_directory}") 
 