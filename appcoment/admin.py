from django.contrib import admin

from .models import PostModel, CommentList, Com

admin.site.register(PostModel)
admin.site.register(CommentList)
admin.site.register(Com)
