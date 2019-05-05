from django.contrib import admin
from users.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'staff_position', 'to_show')


admin.site.register(Profile, ProfileAdmin)

