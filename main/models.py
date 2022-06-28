from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_delete
import os


class Video(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    video_file = models.FileField(upload_to='static/videos/')
    created_at = models.DateField()

    def filepath(self):
        return f'videos/{os.path.basename(self.video_file.name)}'

@receiver(post_delete, sender=Video, weak=False)
def post_save_file(sender, instance, *args, **kwargs):
    """ Clean Old file """
    print('Clean Old file')
    try:
        instance.video_file.delete(save=False)
    except Exception as e:
        print('File delete error,', e)

@receiver(pre_save, sender=Video, weak=False)
def pre_save_file(sender, instance, *args, **kwargs):
    """ instance old file will delete from os """
    print('Clean Old file')
    try:
        old_file = instance.__class__.objects.get(id=instance.id).video_file.path
        try:
            new_file = instance.video_file.path
        except:
            new_file = None
        if new_file != old_file:
            import os
            if os.path.exists(old_file):
                os.remove(old_file)
    except Exception as e:
        print('File delete error,', e)

class Article(models.Model):
    article_type = (
        ('cto', '人物專訪'),
        ('vlog', '轉型日記'),
        ('newinfo', '新知報導'),
    )
    article_image = models.ImageField(upload_to="static/articles/cover/", null=False, blank=False, default="")
    title = models.CharField(max_length=255, null=False)
    context = models.TextField()
    html = models.FileField(upload_to="static/articles/", max_length=100, null=False)
    category = models.CharField(max_length=255, choices=article_type)
    created_at = models.DateField()

    def filename(self):
        return os.path.basename(self.html.name)

    def filepath(self):
        return f'article/{self.filename}'

@receiver(post_delete, sender=Article, weak=False)
def post_save_file(sender, instance, *args, **kwargs):
    """ Clean Old file """
    print('Clean Old file')
    try:
        instance.article_image.delete(save=False)
        instance.html.delete(save=False)
    except Exception as e:
        print('File delete error,', e)

@receiver(pre_save, sender=Article, weak=False)
def pre_save_file(sender, instance, *args, **kwargs):
    """ instance old file will delete from os """
    print('Clean Old file')
    try:
        old_img = instance.__class__.objects.get(id=instance.id).article_image.path
        old_html = instance.__class__.objects.get(id=instance.id).html.path

        try:
            new_img = instance.article_image.path
        except:
            new_img = None
        if new_img != old_img:
            import os
            if os.path.exists(old_img):
                os.remove(old_img)

        try:
            new_html = instance.html.path
        except:
            new_html = None
        if new_html != old_html:
            import os
            if os.path.exists(old_html):
                os.remove(old_html)
    except Exception as e:
        print('File delete error,', e)

class ArticleImage(models.Model):
    post = models.ForeignKey(Article, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = "static/articles/content/")

@receiver(post_delete, sender=ArticleImage, weak=False)
def post_save_file(sender, instance, *args, **kwargs):
    """ Clean Old file """
    print('Clean Old file')
    try:
        instance.images.delete(save=False)
    except Exception as e:
        print('File delete error,', e)

@receiver(pre_save, sender=ArticleImage, weak=False)
def pre_save_file(sender, instance, *args, **kwargs):
    """ instance old file will delete from os """
    print('Clean Old file')
    try:
        old_img = instance.__class__.objects.get(id=instance.id).images.path

        try:
            new_img = instance.images.path
        except:
            new_img = None
        if new_img != old_img:
            import os
            if os.path.exists(old_img):
                os.remove(old_img)
    except Exception as e:
        print('File delete error,', e)


class Feature(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    sub_title = models.CharField(max_length=50, null=False, blank=False)
    html = models.FileField(upload_to='static/features/')
    created_at = models.DateField(auto_now_add=True)

    def filepath(self):
        return f'features/{os.path.basename(self.html.name)}'

@receiver(post_delete, sender=Feature, weak=False)
def post_save_file(sender, instance, *args, **kwargs):
    """ Clean Old file """
    print('Clean Old file')
    try:
        instance.html.delete(save=False)
    except Exception as e:
        print('File delete error,', e)

@receiver(pre_save, sender=Feature, weak=False)
def pre_save_file(sender, instance, *args, **kwargs):
    """ instance old file will delete from os """
    print('Clean Old file')
    try:
        old_file = instance.__class__.objects.get(id=instance.id).html.path
        try:
            new_file = instance.html.path
        except:
            new_file = None
        if new_file != old_file:
            import os
            if os.path.exists(old_file):
                os.remove(old_file)
    except Exception as e:
        print('File delete error,', e)


class FeatureImage(models.Model):
    post = models.ForeignKey(Feature, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = "static/features/content/")

@receiver(post_delete, sender=FeatureImage, weak=False)
def post_save_file(sender, instance, *args, **kwargs):
    """ Clean Old file """
    print('Clean Old file')
    try:
        instance.images.delete(save=False)
    except Exception as e:
        print('File delete error,', e)

@receiver(pre_save, sender=FeatureImage, weak=False)
def pre_save_file(sender, instance, *args, **kwargs):
    """ instance old file will delete from os """
    print('Clean Old file')
    try:
        old_img = instance.__class__.objects.get(id=instance.id).images.path

        try:
            new_img = instance.images.path
        except:
            new_img = None
        if new_img != old_img:
            import os
            if os.path.exists(old_img):
                os.remove(old_img)
    except Exception as e:
        print('File delete error,', e)
