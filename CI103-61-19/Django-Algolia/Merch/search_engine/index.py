# index.py

from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from .models import Memes

@register(Memes)
class MemesIndex(AlgoliaIndex):
    fields = ('pictureName', 'url','description','tag_list','id')
    settings = {'searchableAttributes': ['pictureName','description','tag_list']}
    index_name = 'memes_index'