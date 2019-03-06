from django.contrib import admin
from mainpage.models import File, User, News, Project


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'pub_date', 'user', 'headline',
                    'text', 'main_image')


class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'file_name', 'file_path',
                    'connector_to_news', 'project_name')


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'nick_name', 'email', 'password')


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'description')


admin.site.register(News, NewsAdmin)
admin.site.register(File, FileAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Project, ProjectAdmin)
