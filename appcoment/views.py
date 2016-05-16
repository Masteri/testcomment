from django.shortcuts import render_to_response
from .models import CommentAbs, CommentList, Com, PostModel


def newcabs(request):
    autor = CommentList.objects.all()
    comments = Com.objects.all()
    post = PostModel.objects.all()
    return render_to_response('base.html', {'autor': autor, 'post': post, 'comments': comments})