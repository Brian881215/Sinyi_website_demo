from django.urls import path
from sa_page.views import *


urlpatterns = [
    path('', index, name='index'),
    path('usage/', usage, name='usage'),
]
