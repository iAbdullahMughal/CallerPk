from django.conf.urls import url

from caller.ajax.views import phone_number_added, phone_number_scanned, ajax_search

urlpatterns = [
    url('phone_number_scanned', phone_number_scanned, name="phone_number_scanned"),
    url('search', ajax_search, name="ajax_search"),
]
