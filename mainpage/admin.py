from django.contrib import admin
from mainpage.models import File, Profile, News, Project, Comment


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'pub_date', 'user', 'headline', 'text', 'image')
    filter_horizontal = ['zip_file']


class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'path', 'project_name')


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'staff_position', 'to_show')


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'description',
                    'author', 'image', 'genres')
    filter_horizontal = ['staff_name']


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'news', 'text', 'like')


admin.site.register(News, NewsAdmin)
admin.site.register(File, FileAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Comment, CommentAdmin)

