from django.db import models

class TypeInfo(models.Model):
    ttitle=models.CharField(max_length=20)
    isDelete=models.BooleanField(default=False)

class GoodsInfo(models.Model):

