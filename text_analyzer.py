import sys # taking command line inputs
import os # checking the existance of file
from collections import Counter # to count the occurance

def remove_punctuations(word):
    return ''.join(char.lower() for char in word if char.isalnum())


def check_file(filepath):
    if not os.path.exists(filepath):
        print(f" File not found : {filepath}")
        return
    
    with open(filepath, 'r', encoding= 'utf-8') as f :
        contents = f.read()

    if not contents.strip():
        print(f"The file '{filepath}' is empty.")
        return
    
    lines = contents.splitlines()
    line_count = len(lines)
    print(f" Total lines : {line_count}")


    words = [remove_punctuations(word) for line in lines for word in line.split()]
    words = list(filter(None,words)) # to remove empty words
    count_words = len(words)
    print(f" Total Words: {count_words}")
