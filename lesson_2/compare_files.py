#!/usr/bin/env python

import filecmp

# Example directories
dir1 = '/home/natali/for_python/git/lesson_2/dir1'
dir2 = '/home/natali/for_python/git/lesson_2/dir2'

# Create a directory comparison object
comparison = filecmp.dircmp(dir1, dir2)

# Access comparison results
print(f"Common files: {comparison.common}")
print(f"Files only in {dir1}: {comparison.left_only}")
print(f"Files only in {dir2}: {comparison.right_only}")
print(f"Differences between common files: {comparison.diff_files}")

# Optionally, print a comparison report
comparison.report()
 
