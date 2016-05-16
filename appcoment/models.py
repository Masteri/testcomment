from __future__ import unicode_literals

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

#http://proft.me/2010/09/7/drevovidnye-struktury-dannyh-v-django/
@python_2_unicode_compatible
class PostModel(models.Model):
    title = models.CharField(max_length=200)
    conten = models.TextField()
    timecreated = models.DateTimeField(verbose_name='Data Created', auto_now_add=True)

    def __str__(self):
        return self.title


class CommentAbs(models.Model):
    textcomment = models.CharField(max_length=100)
    likecom = models.CharField(max_length=1, default='+')
    parent = models.ForeignKey('self', blank=True, null=True, verbose_name="Parent", related_name='child')

    def __str__(self):
        return self.textcomment

    class Meta:
        abstract = True



@python_2_unicode_compatible
class CommentList(CommentAbs):
    autor = models.ForeignKey(User)
    comtopost = models.ForeignKey(PostModel, default=1)

    def get_absolute_url(self):
        return "/post/%i/" % self.pk

    def __str__(self):
        return self.textcomment


class Com(models.Model):
    comtopost = models.ForeignKey(CommentList)

    """    def __str__(self):
        return self.pk


class FooModel(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children')
    children = models.ManyToOneRel('self', blank=True, null=True)

    def __init__(self, *args, **kwargs):
        super(FooModel, self).__init__(*args, **kwargs)
        self.parent.children.add(self)
"""