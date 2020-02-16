import numpy as np
from pathlib import Path


class Scrabble:
    def match(self, candidates):
        return np.isin(candidates, self.words)

    def __init__(self, file_path):
        dict_file = open(Path(file_path))
        self.words = np.array(dict_file.read().split())
        self.length = self.words.size
