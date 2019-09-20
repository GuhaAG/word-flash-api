import csv
import collections
import os

from wordflash.settings import BASE_DIR
from rest_framework import status
from rest_framework.test import APITestCase

from . import WordPair

local_file_path = os.path.join(BASE_DIR, 'drive-downloads/wordpairs.csv')


class WordPairTestCase(APITestCase):

    def test_Wordpair_endpoint_health(self):
        response = self.client.get('/wordpair/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_Wordpair_endpoint(self):
        response = self.client.get('/wordpair/')

        wordpairs = []

        with open(local_file_path, mode='r') as infile:
            reader = csv.reader(infile)
            for row in reader:
                jp, en = row
                wordpairs.append(collections.OrderedDict(
                    [('key_en', en), ('key_jp', jp)]))

        infile.close()

        self.assertEqual(response.data, wordpairs)
