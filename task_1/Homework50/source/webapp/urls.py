from django.urls import path

from webapp.views.base import *

app_name = 'webapp'

urlpatterns = [
    path("", index_view),
    path('stats/', stats, name='stats')
]
