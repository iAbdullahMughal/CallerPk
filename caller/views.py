from django.shortcuts import render

# Create your views here.
from caller.core.search.search_record import SearchRecord


def home(request):
    return render(request, 'pages/home/index.html')


def search(request):
    return render(request, 'pages/search/index.html')