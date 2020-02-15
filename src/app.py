import os
from pathlib import Path

os.chdir('./src')


def import_dictionary(file_path):
    dict_file = open(Path(file_path))
    dictionary = list(dict_file.read().split())
    return dictionary


dict = import_dictionary('./dictionary/scrabble_words.txt')

while(True):
    print(dict)
