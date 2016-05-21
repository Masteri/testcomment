from django.views.generic import ListView
from django.shortcuts import render_to_response, get_object_or_404
from .models import  CommentList, PostModel, Genre
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext


def show_genres(request):
    return render_to_response("genres.html",
                          { 'nodes': CommentList.objects.all()},
                          context_instance=RequestContext(request))



def postcoments(request, pk):
    post = PostModel.objects.filter(pk=pk)
    #allcom = CommentList.objects.all()
    contact_list = CommentList.objects.select_related('textcom').filter(textcom=pk)
    paginator = Paginator(contact_list, 5) # Show 5 contacts per page

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

    return render_to_response('postcoments.html', {"contacts": contacts, 'post': post, 'nodes': contacts}
                              , context_instance=RequestContext(request))


def lpost(request, pk):
    post = PostModel.objects.filter(pk=pk)
    comls = CommentList.objects.select_related('textcom').filter(textcom=pk)
    allcom = CommentList.objects.all()
    contact_list = CommentList.objects.select_related('textcom').filter(textcom=pk)
    paginator = Paginator(contact_list, 5) # Show 5 contacts per page

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

    return render_to_response('list.html', {"contacts": contacts, 'comls': comls, 'post': post, 'allcom': allcom})


def newcabspk(request, pk):
    post = PostModel.objects.filter(pk=pk)
    comls = CommentList.objects.select_related('textcom').filter(textcom=pk)
    allcom = CommentList.objects.all()
    return render_to_response('postcom.html', {'comls': comls, 'post': post, 'allcom': allcom})

#https://www.sitepoint.com/hierarchical-data-database/
#http://py-algorithm.blogspot.com/2011/07/blog-post_30.html
#http://proft.me/2010/09/7/drevovidnye-struktury-dannyh-v-django/

def listing(request):
    contact_list = CommentList.objects.all()
    paginator = Paginator(contact_list, 5) # Show 5 contacts per page

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
