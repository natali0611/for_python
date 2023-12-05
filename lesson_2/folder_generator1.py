#!/usr/bin//env python
'''Create a target folder if not exists
function which create 10 folders inside(10 is default value, funcsion should have input argument with folders quantity)
main part which create 10 folders and then 10 folders inside each one.'''

import os 
 
def generate_root_folder(root_folder): 
    if not os.path.exists(root_folder): 
        os.makedirs(root_folder)  
    else: 
        print(f"'{root_folder}' already exsist.") 
 
def generate_sub_folders(sub_folder):
    for i in range(10): 
        folder_name = f"test_{i}"
        folder_path = os.path.join(sub_folder, folder_name)
        os.makedirs(folder_path)
         
def main(): 
    root_folder = "tmp" 
    generate_root_folder(root_folder) 
    generate_sub_folders(root_folder) 
    for i in range(10): 
        multi_folder = os.path.join(root_folder, f"test_{i}") 
        generate_sub_folders(multi_folder) 
 
if __name__ == "__main__": 
    main() 
 