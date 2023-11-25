#!/usr/bin//env python
import sys 
 
def generate(file, phrase, count): 
    with open(file, 'w') as file: 
        for i in range(count): 
            file.write(phrase + '') 
 
if __name__ == "__main__": 
    if len(sys.argv) != 4: 
        print("Error") 
    else: 
        file = sys.argv[1] 
        phrase = sys.argv[2] 
        count = int(sys.argv[3]) 
        generate(file, phrase, count) 
    