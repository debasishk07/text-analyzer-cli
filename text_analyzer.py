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
        print(f" The file '{filepath}' is empty.")
        return
    
    # counting the lines
    lines = contents.splitlines()
    line_count = contents.count(".") 
    print(f"\n Total lines : {line_count}")


    words = [remove_punctuations(word) for line in lines for word in line.split()]
    words = list(filter(None,words)) # to remove empty words
    count_words = len(words)
    print(f" Total Words: {count_words}")

    char_count_with_spaces = len(contents)
    print(f" Total characters with spaces : {char_count_with_spaces}")

    char_without_spaces = len(contents.replace(" ","").replace("\n",""))
    print(f" Character without spaces : {char_without_spaces}")

    print(f" Top 3 most Frequent words are : ")
    word_freq = Counter(words).most_common(3)
    for word, count in word_freq:
        print(f"> {word} : {count} Times")
    
# Bonus findings
    print(f"\n Bonus Findings: ")
    print(f" The average line length : {char_count_with_spaces/line_count:.2f}")
    print(f" Average word length is : {sum(len(w) for w in words)/count_words:.2f}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python text_analyzer.py <file.txt>")
    else:
        check_file(sys.argv[1])

print("\n")