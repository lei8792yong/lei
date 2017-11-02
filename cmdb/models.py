# _*_ coding:utf-8 _*_
from django.db import models
from serversys.models import *
from django.utils import timezone


# Create your models here.
class cmdb(models.Model):
    type = models.CharField(max_length=100,null=True)
    cpu = models.CharField('CPU',max_length=100,null=True)
    motherboard = models.CharField('主板',max_length=100,null=True)
    memory = models.CharField('内存条',max_length=100,null=True)
    graphics = models.CharField('显卡',max_length=100,null=True)
    hard_disk1 = models.CharField('硬盘1',max_length=100,null=True)
    keyboard = models.CharField('键盘/鼠标',max_length=100,null=True)
    chassis = models.CharField('机箱',max_length=100,null=True)
    power_supply = models.CharField('电源',max_length=100,null=True)
    monitor = models.CharField('显示器',max_length=100,null=True)
    who_uses = models.CharField('使用者',max_length=100,null=True)
    price = models.IntegerField('采购价',max_length=100,null=True)
    supplier = models.ForeignKey('group_supplier')         #供应商
    dept = models.ForeignKey(Dept, null=True, blank=True)  #部门
    create_Date = models.DateTimeField(default=timezone.now,null=True)
    comment = models.TextField(blank=True, null=True,max_length=500)

    def __unicode__(self):
        return self.cpu

class group_supplier(models.Model):
    supplier_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)

    def __unicode__(self):
        return self.supplier_name
