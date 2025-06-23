import sys # taking command line inputs
import os # checking the existance of file
from collections import Counter # to count the occurance

def remove_punctuations(word):
    return ''.join(char.lower() for char in word if char.isalnum())

