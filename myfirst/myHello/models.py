from __future__ import unicode_literals

from django.db import models

# Create your models here.
class MySite(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    headimg = models.URLField()
    realName = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
