import itertools
import numpy as np
from pathlib import Path


class Scrabble:
    def match(self, candidates):
        return np.isin(candidates, self.words)

    def __init__(self, file_path):
        dict_file = open(Path(file_path))
        self.words = np.array(dict_file.read().split())
        self.length = self.words.size


def str_to_array(string):
    char_array = np.array([])
    for char in string:
        char_array = np.append(char_array, char)
    return char_array


def candidate_list(input_array):
    candidates = np.array([])
    for i in range(input_array.size):
        perms = itertools.permutations(input_array, i + 1)
        for p in perms:
            candidate = ''
            for char in p:
                candidate += char
            candidates = np.append(candidates, candidate)
    return np.unique(candidates)


dict = Scrabble('./dictionary/scrabble_words_collins_2019.txt')
print('Solving using a dictionary of ' + str(dict.length) + ' words.')

while(__name__ == '__main__'):
    input_string = input('Available characters? ').upper()
    input_array = str_to_array(input_string)

    candidates = candidate_list(input_array)
    match_array = dict.match(candidates)

    for i in range(match_array.size):
        if match_array[i]:
            print(candidates[i])
