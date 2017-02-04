from __future__ import unicode_literals

from django.db import models

# Create your models here.

class school_detail(models.Model):
    school_name = models.CharField(max_length=300)
    # school




class campus_detail(models.Model):
    school_detail = models.ForeignKey(school_detail, on_delete=models.CASCADE())
    campus_name = models.CharField(max_length=100)