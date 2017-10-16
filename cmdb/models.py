from django.db import models

# Create your models here.
class Account(models.Model):
    SN = models.CharField("序列号",max_length=30)
    Business = models.CharField("所属业务",max_length=100)
    IP = models.GenericIPAddressField("公网IP",blank=True,null=True)
    Inner_IP = models.GenericIPAddressField("内网IP",blank=True,null=True)
    User = models.CharField("用户名",max_length=30)
    Passwd = models.CharField("密码",max_length=200)
    Port = models.CharField("端口",max_length=30)
    Landing_mode = models.CharField("登陆方式",max_length=30)
    Create_Date = models.DateTimeField('创建时间')

    def __unicode__(self):
        return u'%s %s %s %s %s %s %s %s %s' % (self.SN,self.Business,self.IP,self.Inner_IP,self.User,self.Passwd,self.Port,self.Landing_mode,self.Create_Date)

class cmdb(models.Model):
    SN = models.CharField('序列号',max_length=30)
    Business = models.ForeignKey('Group_cmdb')
    CPU = models.CharField('CPU',max_length=100)
    Fan = models.CharField('风扇',max_length=100)
    Motherboard = models.CharField('主板',max_length=100)
    Memory = models.CharField('内存条',max_length=100)
    Graphics = models.CharField('显卡',max_length=100)
    Hard_disk1 = models.CharField('硬盘1',max_length=100)
    Hard_disk2 = models.CharField('硬盘2',max_length=100)
    Keyboard = models.CharField('键盘',max_length=100)
    Mouse = models.CharField('鼠标',max_length=100)
    Chassis = models.CharField('机箱',max_length=100)
    Power_Supply = models.CharField('电源',max_length=100)
    Monitor = models.CharField('显示器',max_length=100)
    Who_uses = models.CharField('使用者',max_length=100)
    Price = models.IntegerField('采购价',max_length=100)
    Supplier = models.ForeignKey('Group_Supplier')
    Create_Date = models.DateTimeField('创建时间')

    def __unicode__(self):
        return u'%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s' % (self.SN,self.Business,self.CPU,self.Fan,self.Motherboard,self.Memory,self.Graphics,self.Hard_disk1,self.Hard_disk2,
                                                              self.Keyboard,self.Mouse,self.Chassis,self.Power_Supply,self.Monitor,self.Who_uses,self.Supplier,self.Create_Date)

class Group_cmdb(models.Model):
    Group_name = models.CharField('组名',max_length=100)

    def __unicode__(self):
        return u'%s' % (self.Group_name)

class Group_Supplier(models.Model):
    Supplier_name = models.CharField('供应商',max_length=100)
    Phone = models.IntegerField('联系方式',max_length=100)

    def __unicode__(self):
        return u'%s %s' % (self.Supplier_name,self.Phone)
