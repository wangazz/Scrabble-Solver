from app_components import Scrabble
import itertools
import numpy as np
import pandas as pd
from pathlib import Path

dictionary = Scrabble('./dictionary/scrabble_words_collins_2019.txt')
points_schema_file = Path('./dictionary/points_schema.csv')
points_schema = pd.read_csv(points_schema_file, delimiter=',', index_col='char')


def calculate_points(word, schema):
    points = 0
    for char in word:
        row = points_schema.loc[char]
        points += row['points']
    return points


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


def str_to_array(string):
    char_array = np.array([])
    for char in string:
        char_array = np.append(char_array, char)
    return char_array


print('Solving using a dictionary of ' + str(dictionary.length) + ' words.')

while(__name__ == '__main__'):
    input_string = input('Available characters? ').upper()
    input_array = str_to_array(input_string)

    candidates = candidate_list(input_array)
    match_array = dictionary.match(candidates)

    results_list = np.array([])
    for i in range(match_array.size):
        if match_array[i]:
            results_list = np.append(results_list, candidates[i])

    points_list = np.array([])
    for result in results_list:
        points = calculate_points(result, points_schema)
        points_list = np.append(points_list, points)

    df = pd.DataFrame([results_list, points_list]).T
    df.columns = ['word', 'points']
    results = df.sort_values(by='points', ascending=False)
    print(results)
