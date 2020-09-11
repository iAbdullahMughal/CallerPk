from django.conf.urls import url
from django.urls import path

from caller.views import home, search

urlpatterns = [
    path('', home, name='home_index'),
    path('search/', search, name='search_index'),
]
