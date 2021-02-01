from django.contrib import admin

from .models import Profile, Report, Ban, AvatarImage

admin.site.register(Profile)
admin.site.register(Report)
admin.site.register(Ban)
admin.site.register(AvatarImage)