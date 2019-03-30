from django.db import models

# Create your models here.


class Qiukua(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    content = models.CharField(max_length=50)
    owner = models.CharField(max_length=100)
    money = models.FloatField()
    createtime = models.IntegerField(verbose_name='创建时间戳')
    status = models.BooleanField()
    updatetime = models.DateTimeField(auto_now=True)


class Kua(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    qiukua = models.IntegerField()
    content = models.CharField(max_length=50)
    owner = models.CharField(max_length=100)
    createtime = models.IntegerField(verbose_name='创建时间戳')
    status = models.BooleanField()
    updatetime = models.DateTimeField(auto_now=True)


class Zan(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    kua = models.IntegerField()
    owner = models.CharField(max_length=100)
    createtime = models.IntegerField(verbose_name='创建时间戳')



