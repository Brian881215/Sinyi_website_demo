from django.shortcuts import render
from .models import Video, Article
from django.templatetags.static import static
from django.http import HttpResponse
import requests
from django.template import Template, Context

# Create your views here.


def index(request):
    return render(request, 'index.html', locals())

def video(request):
    videos = Video.objects.exclude(filename='index.mp4').order_by('-created_at')
    return render(request, 'video.html', {'videos': videos})

def article(request):
    articles = Article.objects.all().order_by('-datetime')
    latest_article = Article.objects.order_by('datetime').last
    context = {'articles':articles, 'latest_article':latest_article}
    return render(request, 'article.html', context)

def article_details(request,pk):
    article = Article.objects.get(pk=pk)
    html_path = str(article.html)
    response = requests.get(static(html_path))
    response.encoding = 'utf-8'
    template = Template(response.text)

    return HttpResponse(template.render(Context(locals())))