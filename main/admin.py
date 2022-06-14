from django.contrib import admin
from .models import Video, Article, ArticleImage

# admin.site.register(Article)
@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'filename')
    search_fields = ('title', )

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

class ArticleImageAdmin(admin.StackedInline):
    model = ArticleImage

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleImageAdmin]
 
    class Meta:
       model = Article