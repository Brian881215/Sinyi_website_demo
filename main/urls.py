from django.urls import path
from main.views import *


urlpatterns = [
    path('', index, name='index'),
    path('video/', video, name='video'),
    path('article/', article, name='article'),
    path('article/<int:pk>', article_details, name='article_details'),
    path('feature/', feature, name='feature'),
    path('feature/<int:pk>', feature_details, name='feature_details'),
]
