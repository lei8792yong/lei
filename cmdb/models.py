# _*_ coding:utf-8 _*_
from django.db import models
from serversys.models import *

# Create your models here.
class account(models.Model):
    Business = models.CharField("所属业务",max_length=100)
    ip = models.GenericIPAddressField("公网IP",blank=True,null=True)
    inner_ip = models.GenericIPAddressField("内网IP",blank=True,null=True)
    user = models.CharField("用户名",max_length=30)
    passwd = models.CharField("密码",max_length=200)
    port = models.CharField("端口",max_length=30)
    landing_mode = models.CharField("登陆方式",max_length=30)
    create_date = models.DateTimeField('创建时间')

    def __unicode__(self):
        return self.SN

class cmdb(models.Model):
    cpu = models.CharField('CPU',max_length=100)
    fan = models.CharField('风扇',max_length=100)
    motherboard = models.CharField('主板',max_length=100)
    memory = models.CharField('内存条',max_length=100)
    graphics = models.CharField('显卡',max_length=100)
    hard_disk1 = models.CharField('硬盘1',max_length=100)
    keyboard = models.CharField('键盘/鼠标',max_length=100)
    chassis = models.CharField('机箱',max_length=100)
    power_Supply = models.CharField('电源',max_length=100)
    monitor = models.CharField('显示器',max_length=100)
    who_uses = models.CharField('使用者',max_length=100)
    price = models.IntegerField('采购价',max_length=100)
    supplier = models.ForeignKey('Group_Supplier')         #供应商
    dept = models.ForeignKey(Dept, null=True, blank=True)  #部门
    create_Date = models.DateTimeField('创建时间')
    comment = models.TextField(blank=True, null=True,max_length=500)

    def __unicode__(self):
        return self.SN

class group_supplier(models.Model):
    supplier_name = models.CharField('供应商',max_length=100)
    phone = models.IntegerField('联系方式',max_length=100)
