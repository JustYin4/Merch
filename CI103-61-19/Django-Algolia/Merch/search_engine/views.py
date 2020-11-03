from django.shortcuts import render
from django.http import HttpResponse
from algoliasearch_django import raw_search
from .models import Memes
# Create your views here.

def homepage(request):
        if "submit" in request.POST:
                params = {"hitsPerPage": 30}
                response = raw_search(Memes, request.POST["search_field"], params)
                meme_dict = []
                for x in response["hits"]:
                        temp = {"pictureName": x["pictureName"],
                                "url": x["url"],
                                "description": x["description"]
                        }
                        meme_dict.append(temp)
        else:
                meme_dict = []
        context = {
                "memes": meme_dict
        }
        return render(request, 'index.html', context)
    
def search(request):
        return render(request, 'index.html')
    