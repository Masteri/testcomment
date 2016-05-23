from django.shortcuts import render_to_response, get_object_or_404
from .models import  CommentList, PostModel
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.shortcuts import redirect
import uuid
import random


def postcoments(request, pk):
    post = PostModel.objects.filter(pk=pk)
    contact_list = CommentList.objects.select_related('textcom').filter(textcom=pk)
    paginator = Paginator(contact_list, 20) # Show 5 contacts per page

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

    return render_to_response('postcoments.html', {"contacts": contacts, 'post': post, 'nodes': contacts})


def post_update(request, pk):
    if CommentList.objects.filter(pk=pk, likecom='-'):
        CommentList.objects.filter(pk=pk).update(likecom='+')
    elif CommentList.objects.filter(pk=pk, likecom='+'):
        CommentList.objects.filter(pk=pk).update(likecom='-')
    return redirect('/')



def newcabspk(request, pk):
    post = PostModel.objects.filter(pk=pk)
    comls = CommentList.objects.select_related('textcom').filter(textcom=pk)
    allcom = CommentList.objects.all()
    return render_to_response('postcom.html', {'comls': comls, 'post': post, 'allcom': allcom})



def index(request):
    comls = CommentList.objects.all()
    post = PostModel.objects.all()
    counter = CommentList.objects.count()
    return render_to_response('base.html', {'comls': comls, 'post': post, 'counter': counter})


def postaddrows(request):
    autor = User.objects.get()
    for i in range(0, 5):                                                                  #!!!creating some Post in range
        title = 'Title New:   ' + (str(uuid.uuid4()))                                      #creating random string for title
        conten = 'Content New:   ' + (str(uuid.uuid4()))                                   #creating random string for content
        PostModel.objects.create(title = title, conten= conten)                            #add to data Post
        allpost = PostModel.objects.all()                                                  #get all Posts

        for c in allpost:                                                                  #!!!for all Posts generating comments (Parrent)
            i = 0
            r = random.randint(1, 2)
            while i < r:
                textcomment = 'Comment Text Content New:   ' + (str(uuid.uuid4()))
                textcom = PostModel.objects.get(pk=c.pk)
                CommentList.objects.create(textcomment=textcomment, autor=autor, textcom=textcom)
                i = i + 1

            p = CommentList.objects.all()[:100]
            for a in p:
                textcomment = 'I\'m chield Comment Text Content New:   ' + (str(uuid.uuid4()))
                compost = PostModel.objects.get(pk=c.pk)
                CommentList.objects.create(textcomment=textcomment, autor=autor, textcom=compost).move_to(a)

    post = PostModel.objects.all()
    counter = CommentList.objects.count()
    return render_to_response('base.html', {'post': post, 'counter': counter})