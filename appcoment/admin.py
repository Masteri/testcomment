from django.contrib import admin

from .models import PostModel, CommentList


admin.site.register(PostModel)
admin.site.register(CommentList)


