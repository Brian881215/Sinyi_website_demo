from django.shortcuts import render
from .models import Video, Article, Feature
from django.http import HttpResponse
import requests
from django.template import Template, Context
import os
from django.contrib.auth.models import User, Permission
from datetime import datetime


def index(request):
    creatuser()

    features = Feature.objects.order_by('-created_at')
    showUpArticle = Article.objects.all().order_by('-created_at')[:8]
    for article in showUpArticle:
        article.created_at = datetime.strftime(article.created_at, '%Y-%m-%d')
    index_video = Video.objects.filter(is_index=True).order_by('-created_at').first()
    return render(request, 'index.html', locals())

def video(request):
    videos = Video.objects.order_by('-created_at')
    for video in videos:
        video.created_at = datetime.strftime(video.created_at, '%Y-%m-%d')
    return render(request, 'video.html', {'videos': videos})

def article(request):
    articles = Article.objects.all().order_by('-created_at')
    for article in articles:
        article.created_at = datetime.strftime(article.created_at, '%Y-%m-%d')
    latest_article = Article.objects.order_by('-created_at').first()
    latest_article.created_at = datetime.strftime(latest_article.created_at, '%Y-%m-%d')
    context = {'articles':articles, 'latest_article':latest_article}
    return render(request, 'article.html', context)

def article_details(request, pk):
    article = Article.objects.get(pk=pk)
    html_path = request.build_absolute_uri(f'/{str(article.html)}')
    response = requests.get(html_path)
    response.encoding = 'utf-8'
    template = Template(response.text)

    return HttpResponse(template.render(Context(locals())))

def feature(request):
    features = Feature.objects.order_by('-created_at')
    return render(request, 'feature.html', {'features': features})

def feature_details(request, pk):
    feature = Feature.objects.get(pk=pk)
    html_path = request.build_absolute_uri(f'/{str(feature.html)}')
    response = requests.get(html_path)
    response.encoding = 'utf-8'
    template = Template(response.text)

    return HttpResponse(template.render(Context(locals())))

def creatuser():
    if not User.objects.exists():
        print('There is no user on the admin site. Automatically create user...')

        # create super user
        User.objects.create_user(username = os.environ['ROOT_USER'],
                                email = os.environ['ROOT_EMAIL'],
                                password = os.environ['ROOT_PWD'],
                                is_staff = True,
                                is_active = True,
                                is_superuser = True
                                )

        # create TO user
        to_user = User.objects.create_user(username = os.environ['TO_USER'],
                                email = '',
                                password = os.environ['TO_PWD'],
                                is_staff = True,
                                is_active = True,
                                )
        to_perm = Permission.objects.filter(codename__in=['add_video', 'view_video', 'change_video', 'delete_video',
                                                        'add_article', 'view_article', 'change_article', 'delete_article',
                                                        'add_articleimage', 'view_articleimage', 'change_articleimage', 'delete_articleimage',
                                                        'add_feature', 'view_feature', 'change_feature', 'delete_feature',
                                                        'add_featureimage', 'view_featureimage', 'change_featureimage', 'delete_featureimage',])
        to_user.user_permissions.set(to_perm)
