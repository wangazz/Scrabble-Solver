import numpy as np
from pathlib import Path


class Scrabble:
    def match(self, chars):  # todo
        self.words
        matches = np.array()
        return matches

    def __init__(self, file_path):
        dict_file = open(Path(file_path))
        self.words = np.array(dict_file.read().split())
        self.length = self.words.size


dict = Scrabble('./dictionary/scrabble_words.txt')
print('Solving using a dictionary of ' + str(dict.length) + ' words.')

while(True):
    input_chars = input('Available characters? ').lower()
    matches = dict.match(input_chars)
    for i in matches.size:
        print(matches[i])
    input('Press enter to search again.')
