from django.http import HttpResponse
from django.views.generic import ListView
from django.shortcuts import render_to_response,get_object_or_404
from .models import CommentAbs, CommentList, PostModel
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def newcabspk(request, pk):
    post = PostModel.objects.filter(pk=pk)
    comls = CommentList.objects.select_related('textcom').filter(textcom=pk)
    allcom = CommentList.objects.all()
    #comls = CommentList.objects.filter(parent_id=pk)#.select_related().all()
    #comls = CommentList.objects.filter(pk=comid)
    return render_to_response('postcom.html', {'comls': comls, 'post': post, 'allcom': allcom})

def listing(request):
    contact_list = CommentList.objects.all()
    paginator = Paginator(contact_list, 25) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        #http://djbook.ru/rel1.8/topics/pagination.html#using-paginator-in-a-view
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    return render_to_response('list.html', {"contacts": contacts})

def newcabs(request):
    comls = CommentList.objects.all()
    post = PostModel.objects.all()
    return render_to_response('base.html', {'comls': comls, 'post': post})


class ComentListView(ListView):
    model = CommentList

    def head(self,*args, **kwargs):
        post = PostModel.objects.all()
        return render_to_response('base.html', {'post': post})
