from .models import Comment, Interest, Post, PostImage, BookMark
from django.contrib import admin

admin.site.register(Post)
admin.site.register(Interest)
admin.site.register(Comment)
admin.site.register(PostImage)
admin.site.register(BookMark)