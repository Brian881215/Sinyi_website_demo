from django.urls import path
from .views import *

# from .views import ArticleView

urlpatterns = [
    path('', index, name='index'),
    path('video/', video, name='video'),
    path('doc/', doc, name='doc'),
    path('article/', article, name='article'),
    path('article/<int:pk>', article_details, name='article_details'),
]
