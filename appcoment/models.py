from __future__ import unicode_literals

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey
from django.core.urlresolvers import reverse

class Genre(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

    class MPTTMeta:
        order_insertion_by = ['name']


#http://proft.me/2010/09/7/drevovidnye-struktury-dannyh-v-django/

@python_2_unicode_compatible
class PostModel(models.Model):
    title = models.CharField(max_length=200)
    conten = models.TextField()
    timecreated = models.DateTimeField(verbose_name='Data Created', auto_now_add=True)

    def __str__(self):
        return self.title


class CommentAbs(MPTTModel):
    #class CommentAbs(models.Model):
    textcomment = models.CharField(max_length=100)
    likecom = models.CharField(max_length=1, default='+')
    parent = models.ForeignKey('self', blank=True, null=True, verbose_name="parent", related_name='child', db_index=True)

    def __str__(self):
        return self.textcomment

    class Meta:
        abstract = True



@python_2_unicode_compatible
class CommentList(CommentAbs):
    autor = models.ForeignKey(User)
    textcom = models.ForeignKey(PostModel, related_name='postnuber')



    def get_absolute_url(self):
        return  "/postcoments/%i/" % self.pk #reverse('like', kwargs={'pk': self.pk})  #

    def __str__(self):
        return self.textcomment

