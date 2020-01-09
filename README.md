## *** No longer under-development, replaced by `flash-drive` flutter project also on this account ***


-----------------------------------------------------

## Wordflash backend

This is a _simple_ python/django rest framework `REST API` which will read language word pairs from google drive and throw them back.

### Setup and Run for development

- Run `pip3 install -r requirements.txt`
- Place language word pairs in comma separated format in `direct-downloads/wordpairs.csv` (To-do: download from google drive)
- Run `python3 manage.py runserver`
- Point a browser to, or check by curl `http://127.0.0.1:8000/`
- To run tests Run `python3 manage.py test`

[![CircleCI](https://circleci.com/gh/GuhaAG/word-flash-api.svg?style=svg)](https://circleci.com/gh/GuhaAG/word-flash-api)
