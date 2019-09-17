## Wordflash backend

This is a _simple_ python/django rest framework `REST API` which will read language word pairs from google drive and throw them back.

### Setup and Run for development

- Create `virtualenv`
- Activate `virtualenv`
- Run `pip3 install -r requirements.txt`
- Place language word pairs in comma separated format in `direct-downloads/wordpairs.csv` (To-do: download from google drive)
- Run `python3 manage.py runserver`
- Point a browser to, or check by curl `http://127.0.0.1:8000/`
- Deactivate `virtualenv` when done
