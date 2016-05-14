from __future__ import unicode_literals

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

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
    content_type = models.ForeignKey(ContentType,
                                     object_pk = models.TextField(_('object ID'))
                                     )

    class Meta:
        abstract = True


@python_2_unicode_compatible
class CommentList(CommentAbs):
    autor = models.ForeignKey(User)

    def __str__(self):
        return self.textcomment


class Com(models.Model):
    comtopost = models.ForeignKey(CommentList)


