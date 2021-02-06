from .models import Comment, Interest, Post, PostImage, BookMark, Notification
from django.contrib import admin

admin.site.register(Post)
admin.site.register(Interest)
admin.site.register(Comment)
admin.site.register(PostImage)
admin.site.register(BookMark)
admin.site.register(Notification)