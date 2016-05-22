from django.shortcuts import render_to_response, get_object_or_404
from .models import  CommentList, PostModel
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
import uuid
import random


def postcoments(request, pk):
    post = PostModel.objects.filter(pk=pk)
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

    return render_to_response('postcoments.html', {"contacts": contacts, 'post': post, 'nodes': contacts})
                              #, context_instance=RequestContext(request))

def post_update(request, pk):
    instance = get_object_or_404(CommentList, id=pk)
    instance.likecom="-"
    instance.save() #entries = Entry.objects.select_for_update().filter(author=request.user)
    context = {
        "likecom": instance.likecom  #https://www.youtube.com/watch?v=70tK2zjwM50
    }
    return render_to_response('postcoments.html', request, context)



def newcabspk(request, pk):
    post = PostModel.objects.filter(pk=pk)
    comls = CommentList.objects.select_related('textcom').filter(textcom=pk)
    allcom = CommentList.objects.all()
    return render_to_response('postcom.html', {'comls': comls, 'post': post, 'allcom': allcom})



def newcabs(request):
    comls = CommentList.objects.all()
    post = PostModel.objects.all()
    counter = CommentList.objects.count()
    return render_to_response('base.html', {'comls': comls, 'post': post, 'counter': counter})


def postaddrows(request):
    autor = User.objects.get()
    for i in range(0, 10):                                                                 #!!!creating some Post in range 100
        title = 'Title New:   ' + (str(uuid.uuid4()))                                      #creating random string for title
        conten = 'Content New:   ' + (str(uuid.uuid4()))                                   #creating random string for content
        PostModel.objects.create(title = title, conten= conten)                            #add to data Post
        allpost = PostModel.objects.all()                                                  #get all Posts


        for c in allpost:                                                                  #!!!for all Posts generating comments (Parrent)
            i = 0
            r = random.randint(1, 10)
            while i < r:
                textcomment = 'Comment Text Content New:   ' + (str(uuid.uuid4()))
                textcom = PostModel.objects.get(pk=c.pk)
                CommentList.objects.create(textcomment=textcomment, autor=autor, textcom=textcom)
                i = i + 1

            p = CommentList.objects.all()

            #for a in p:
            #cparent = CommentList.objects.select_related('textcom').filter(textcom=a.id)
            rr = random.randint(1, 10)
            cc = 0
            #while cc < rr:
            textcomment = 'Parent? Comment Text Content New:   ' + (str(uuid.uuid4()))
            textcom = PostModel.objects.get(pk=c.pk)
            CommentList.objects.create(textcomment=textcomment, autor=autor, textcom=textcom, parent= c.pk)#a.parent)
                #    cc = cc + 1


    post = PostModel.objects.all()
    counter = CommentList.objects.count()
    return render_to_response('base.html', {'post': post, 'counter': counter})