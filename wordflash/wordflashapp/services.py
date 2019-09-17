import csv
import os
from wordflash.settings import BASE_DIR
from . import WordPair
"""
WordPairs = {
    1: WordPair(id=1, key_en='Yes', key_jp='Hai'),
    2: WordPair(id=2, key_en='No', key_jp='Iie')
}"""


def getWordPairsFromCsv():
    file_path = os.path.join(BASE_DIR, 'drive-downloads/wordpairs.csv')
    wordpairs = {}

    i = 1
    with open(file_path, mode='r') as infile:
        reader = csv.reader(infile)
        for row in reader:
            jp, en = row
            wordpairs[i] = WordPair(key_en=en, key_jp=jp)
            i = i+1

    return wordpairs
