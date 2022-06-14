from django.db import models
import os

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    filename = models.CharField(max_length=50, null=False, blank=False)
    file = models.FileField(upload_to='videos/')
    created_at = models.DateField(null=False, blank=False)

    def filepath(self):
        return f'videos/{self.filename}'

class Article(models.Model):
    article_type = (
        ('人物專訪', '人物專訪'),
        ('轉型日記', '轉型日記'),
        ('新知報導', '新知報導'),
    )
    article_image = models.ImageField(upload_to="images/article/cover/", null=False, blank=False, default="")
    datetime = models.DateField()
    title = models.CharField(max_length=255, null=False)
    context = models.TextField()
    html = models.FileField(upload_to="article/", max_length=100, null=False)
    category = models.CharField(max_length=255, choices=article_type)

    def filename(self):
        return os.path.basename(self.html.name)

    def filepath(self):
        return f'article/{self.filename}'
    
    def __str__(self):
        return os.path.basename(self.html.name)

class ArticleImage(models.Model):
    post = models.ForeignKey(Article, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = "images/article/content/")
 
    def __str__(self):
        return self.images.name