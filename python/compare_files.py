#!/usr/bin/env python
'''Compares two directories and reports the differences between them'''
import filecmp

# Example directories
dir1 = '/home/natali/for_python/git/lesson_2/dir1'
dir2 = '/home/natali/for_python/git/lesson_2/dir2'

# Create a directory comparison object
compar = filecmp.dircmp(dir1, dir2)

# Access comparison results
print(f"Common files: {compar.common}")
print(f"Files only in {dir1}: {compar.left_only}")
print(f"Files only in {dir2}: {compar.right_only}")
print(f"Differences between common files: {compar.diff_files}")

# Optionally, print a comparison report
compar.report()
 