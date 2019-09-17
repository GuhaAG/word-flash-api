class WordPair(object):
    def __init__(self, **kwargs):
        for field in ('id', 'key_en', 'key_jp'):
            setattr(self, field, kwargs.get(field, None))