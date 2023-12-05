#!/usr/bin/env python

'''generate folder with 10 test folders which contains 10 folder inside each, and each folder should have 10 files inside.'''

import random
import os

def generateTenFolders(root_path):
  folder_name = "test"
  for index in range(10):
    os.mkdir(os.path.join(root_path, f"{folder_name}0{index}"))

def generateTenFiles(path):
  for i in range(10):
    value = str(10)
    with open(f"{path}/test0{i}", "w") as file:
      file.write(value)

def createFilesInAllDirTree(path):
  dirlist = os.listdir(path)
  if len(dirlist) != 0:
    for i in os.listdir(path):
      fullpath = os.path.join(path, i)
      if os.path.isdir(fullpath):
        createFilesInAllDirTree(fullpath)
  else:
    generateTenFiles(path)


def main():
  root = "./tmp"
  if not os.path.exists(root):
    os.mkdir(root)

  generateTenFolders(root)
  for i in os.listdir(root):
    generateTenFolders(os.path.join(root, i))

  createFilesInAllDirTree(root)

if __name__ == "__main__":
  main()