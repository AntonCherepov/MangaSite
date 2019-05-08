from django.contrib import admin
from mainpage.models import File, News, Project, Comment


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'pub_date', 'user', 'headline', 'text', 'image')
    filter_horizontal = ['zip_file']


class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'path', 'project_name')


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'description',
                    'author', 'image', 'genres')
    filter_horizontal = ['staff_name']


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'pub_date', 'user', 'news_id', 'text', 'like')


admin.site.register(News, NewsAdmin)
admin.site.register(File, FileAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Comment, CommentAdmin)
