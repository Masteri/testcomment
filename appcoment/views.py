from django.shortcuts import render_to_response
from .models import CommentAbs, CommentList, Com, PostModel


def newcabs(request):
    comls = CommentList.objects.all()
    comments = Com.objects.all()
    post = PostModel.objects.all()
    return render_to_response('base.html', {'comls': comls, 'post': post, 'comments': comments})