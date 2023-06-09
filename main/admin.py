from django.contrib import admin
from .models import Video, Article, ArticleImage, Feature, FeatureImage


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_index', 'filepath', 'created_at')
    search_fields = ('title', )


class ArticleImageAdmin(admin.StackedInline):
    model = ArticleImage


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'filename', 'is_hidden', 'is_index', 'created_at')
    list_filter = ('category', )
    search_fields = ('title', 'category')
    inlines = [ArticleImageAdmin]

    class Meta:
       model = Article


class FeatureImageAdmin(admin.StackedInline):
    model = FeatureImage


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'sub_title', 'filepath', 'order', 'is_hidden')
    search_fields = ('title', )
    inlines = [FeatureImageAdmin]

    class Meta:
       model = Feature
