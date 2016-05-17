from django.http import HttpResponse
from django.views.generic import ListView
from django.shortcuts import render_to_response
from .models import CommentAbs, CommentList, Com, PostModel


def newcabs(request):
    comls = CommentList.objects.all()
    comments = Com.objects.all()
    post = PostModel.objects.all()
    return render_to_response('base.html', {'comls': comls, 'post': post, 'comments': comments})

class ComentListView(ListView):
    model = CommentList

    def head(self,*args, **kwargs):
        post = PostModel.objects.all()
        return render_to_response('base.html', {'post': post})
