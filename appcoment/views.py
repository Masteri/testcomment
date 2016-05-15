from django.shortcuts import render_to_response
from .models import CommentAbs, CommentList, Com


def newcabs(request):
    autor = CommentList.objects.all()
    post = Com.objects.all()

    return render_to_response('base.html', {'autor': autor, 'post': post})