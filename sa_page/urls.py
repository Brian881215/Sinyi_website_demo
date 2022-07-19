from django.urls import path
from sa_page.views import *


urlpatterns = [
    path('', index, name='index'),
    path('pd_data/', usage, name='pd_data'),
    path('voting/', voting, name='voting'),
    path('functionintro/', functionintro, name='functionintro'),
]
