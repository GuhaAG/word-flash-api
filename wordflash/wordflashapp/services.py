import csv
import os
import requests
from wordflash.settings import BASE_DIR
from . import WordPair


"""
WordPairs = {
    1: WordPair(id=1, key_en='Yes', key_jp='Hai'),
    2: WordPair(id=2, key_en='No', key_jp='Iie')
}"""

local_file_path = os.path.join(BASE_DIR, 'drive-downloads/wordpairs.csv')
remote_file_path = 'https://drive.google.com/open?id=1y0njxwAgEo7snlfTj-C_jSpfHc3tKzh88wmg5WuBoe4'


def getWordPairsFromCsv():
    wordpairs = {}

    i = 1
    with open(local_file_path, mode='r') as infile:
        reader = csv.reader(infile)
        for row in reader:
            jp, en = row
            wordpairs[i] = WordPair(key_en=en, key_jp=jp)
            i = i+1

    infile.close()

    return wordpairs


def downloadFileFromGDrive():
    response = requests.get(remote_file_path+'&output=csv')
    print(response.content)
