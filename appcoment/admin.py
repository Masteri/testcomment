from django.contrib import admin

from .models import PostModel, CommentList, Genre

admin.site.register(PostModel)
admin.site.register(CommentList)
admin.site.register(Genre)

