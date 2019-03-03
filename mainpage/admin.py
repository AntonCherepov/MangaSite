from django.contrib import admin
from mainpage.models import File, User, Main


class MainAdmin(admin.ModelAdmin):
    list_display = ('id', 'pub_date', 'user', 'headline', 'text', 'main_image')


class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'file_name', 'file_path', 'connector_to_news')


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'nick_name', 'email', 'password')


admin.site.register(Main, MainAdmin)
admin.site.register(File, FileAdmin)
admin.site.register(User, UserAdmin)
