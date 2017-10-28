# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response,RequestContext

from account.account_api import *
from account.models import *
from serversys.models import *
from cmdb.models import *

import time,datetime
import xlwt
import StringIO

# Create your views here.

@require_login
def cmdb_list(request):
    if request.method == 'GET':
        Username = request.session.get('user_name')
        Cmdb = cmdb.objects.all()

        kwavs = {
            'request':request,
            'username':Username,
            'cmdb':Cmdb,
        }

        return render_to_response('cmdb/cmdb_lists.html',kwavs,RequestContext(request))

@require_login
def cmdb_add(request):
    if request.method == "GET":
        Username = request.session.get('user_name')
        Deptdata = Dept.objects.all()
        Supplier = group_supplier.objects.all()

        kwvars = {
            'request':request,
            'Username': Username,
            'Deptdata': Deptdata,
            'Supplier': Supplier,
        }

        return render_to_response('cmdb/cmdb_add.html',kwvars,RequestContext(request))

    if request.method == "POST":
        cpu = request.POST.get('cpu')
        motherboard = request.POST.get('motherboard')
        memory = request.POST.get('memory')
        graphics = request.POST.get('graphics')
        dept_id = request.POST.get('dept')
        deptname = Dept.objects.get(id=dept_id)
        hard_disk1 = request.POST.get('hard_disk1')
        keyboard = request.POST.get('keyboard')
        chassis = request.POST.get('chassis')
        power_supply = request.POST.get('power_Supply')
        monitor = request.POST.get('monitor')
        who_uses = request.POST.get('who_uses')
        price = request.POST.get('price')
        supplier_id = request.POST.get('supplier')
        supplier = group_supplier.objects.get(id=supplier_id)
        datetime = request.POST.get('datetime')
        description = request.POST.get('description')

        p=cmdb(cpu=cpu,motherboard=motherboard,memory=memory,graphics=graphics,hard_disk1=hard_disk1,keyboard=keyboard,
               chassis=chassis,power_supply=power_supply,monitor=monitor,who_uses=who_uses,price=price,supplier=supplier,dept=deptname,comment=description,create_Date=datetime)
        p.save()
        return HttpResponse(u'添加成功')

@require_login
def cmdb_edit(request,cid):
    if request.method == 'GET':
        Username = request.session.get('user_name')
        Cmdbdata = cmdb.objects.get(id=cid)
        Deptdata = Dept.objects.all()
        Suppdata = group_supplier.objects.all()

        kwvars = {
            'request':request,
            'username':Username,
            'cmdbdata':Cmdbdata,
            'deptdata':Deptdata,
            'suppdata':Suppdata,
        }

        return render_to_response('cmdb/cmdb_edit.html',kwvars,RequestContext(request))

    if request.method == 'POST':
        if is_common_user(request):
            return HttpResponse(u'普通用户没有权限')

        cmdbedit = cmdb.objects.get(id=cid)
        cmdbedit.cpu = request.POST.get('cpu')
        cmdbedit.motherboard = request.POST.get('motherboard')
        cmdbedit.memory = request.POST.get('memory')
        cmdbedit.graphics = request.POST.get('graphics')
        dept_id = request.POST.get('dept')
        cmdbedit.deptname = Dept.objects.get(id=dept_id)
        cmdbedit.hard_disk1 = request.POST.get('hard_disk1')
        cmdbedit.keyboard = request.POST.get('keyboard')
        cmdbedit.chassis = request.POST.get('chassis')
        cmdbedit.power_supply = request.POST.get('power_supply')
        cmdbedit.monitor = request.POST.get('monitor')
        cmdbedit.who_uses = request.POST.get('who_uses')
        cmdbedit.price = request.POST.get('price')
        supplier_id = request.POST.get('supplier')
        cmdbedit.supplier = group_supplier.objects.get(id=supplier_id)
        cmdbedit.datetime = request.POST.get('datetime')
        cmdbedit.comment = request.POST.get('description')
        cmdbedit.save()

        return HttpResponse(u'修改成功')

@require_login
def cmdb_del(request,cid):
    if request.method == 'GET':
        if is_common_user(request):
            return HttpResponse(u'普通用户没有权限')
        cmdb.objects.get(id=cid).delete()
        return HttpResponse(u'资产删除成功')



@require_login
def supplier_list(request):
    if request.method == "GET":
        Username = request.session.get('user_name')
        Supplier = group_supplier.objects.all()

        kwvars = {
            'request':request,
            'Username':Username,
            'Supplier':Supplier,
        }

        return render_to_response('cmdb/supplier_list.html',kwvars,RequestContext(request))

@require_login
def supplier_add(request):
    if request.method == "GET":
        Username = request.session.get('user_name')
        kwvars = {
            'request':request,
            'Username':Username,
        }

        return render_to_response('cmdb/supplier_add.html',kwvars,RequestContext(request))

    if request.method == "POST":
        supplier_name = request.POST.get('dept_name')
        supplier_phone = request.POST.get('dept_phone')

        if group_supplier.objects.filter(supplier_name=supplier_name):
            Warrmess = u'该供应商已存在'
            return HttpResponse(Warning)
        else:
            p = group_supplier(supplier_name=supplier_name,phone=supplier_phone)
            p.save()

            return HttpResponse(u'供应商添加成功')

@require_login
def supplier_del(request,id):
    group_supplier.objects.get(id=id).delete()
    return HttpResponse(u'供应商删除成功!!')

@require_login
def supplier_edit(request,sid):
    if request.method == 'GET':
        Username= request.session.get('user_name')
        getsu = group_supplier.objects.filter(id=sid)

        kwvars = {
            'request':request,
            'username':Username,
            'Sid' : sid,
            'Getsu' : getsu,
        }

        return render_to_response('cmdb/supplier_edit.html',kwvars,RequestContext(request))

    if request.method == 'POST':
        if is_common_user(request):
            return HttpResponse(u"普通用户没有权限!!!")

        GetSuppname=request.POST.get('Supp_edit_name')
        GetSuppphone=request.POST.get('Supp_edit_phone')

        if group_supplier.objects.filter(supplier_name=GetSuppname,phone=GetSuppphone,id=sid):

            GetSept=group_supplier.objects.get(id=sid)
            GetSept.supplier_name=request.POST.get('Supp_edit_name')
            GetSept.phone=request.POST.get('Supp_edit_phone')
            GetSept.save()
            return HttpResponse(u"供应商修改成功 1")

        if group_supplier.objects.filter(supplier_name=GetSuppname):
            return HttpResponse(u"供应商已经存在，请重新输入!!!")
        else:
            GetSept=group_supplier.objects.get(id=sid)
            GetSept.supplier_name=request.POST.get('Supp_edit_name')
            GetSept.phone=request.POST.get('Supp_edit_phone')
            GetSept.save()
            return HttpResponse(u"供应商修改成功 2")

@require_login
def exportAgencyCustomers_cmdb(request):
    datenow=datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d')
    file=datenow+"资产列表.xls"
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment;filename=%s' %file
    wb = xlwt.Workbook(encoding = 'utf-8')

    sheet = wb.add_sheet(str(datenow)+" 资产列表",cell_overwrite_ok=True)
    #1st line
    sheet.write(0,0, 'SN')
    sheet.write(0,1, 'CPU')
    sheet.write(0,2, '主板')
    sheet.write(0,3, '内存条')
    sheet.write(0,4, '显卡')
    sheet.write(0,5, '硬盘')
    sheet.write(0,6, '键盘/鼠标')
    sheet.write(0,7, '机箱')
    sheet.write(0,8, '电源')
    sheet.write(0,9, '显示器')
    sheet.write(0,10, '使用者')
    sheet.write(0,11, '价格')
    sheet.write(0,12, '供应商')
    sheet.write(0,13, '部门')
    sheet.write(0,14, '采购时间')
    sheet.write(0,15, '详细')
    sheet.write(0,16, '添加时间')
    row = 1
    for cmdb in cmdb.objects.all():

        sheet.write(row,0, cmdb.id)
        sheet.write(row,1, cmdb.cpu)
        sheet.write(row,2, cmdb.motherboard)
        sheet.write(row,3, cmdb.memory)
        sheet.write(row,4, cmdb.graphics)
        sheet.write(row,5, cmdb.hard_disk1)
        sheet.write(row,6, cmdb.keyboard)
        sheet.write(row,7, cmdb.chassis)
        sheet.write(row,8, cmdb.power_supply)
        sheet.write(row,9, cmdb.monitor)
        sheet.write(row,10, cmdb.who_uses)
        sheet.write(row,11, cmdb.price)
        sheet.write(row,12, cmdb.supplier.supplier_name)
        sheet.write(row,13, cmdb.dept.name)
        sheet.write(row,14, cmdb.create_Date)
        sheet.write(row,15, cmdb.comment)
        addtimes = datetime.datetime.strftime(cmdb.addtime, '%Y-%m-%d %H:%M:%S')

        sheet.write(row,16, str(addtimes))
        row=row + 1
    output = StringIO.StringIO()
    wb.save(output)
    output.seek(0)
    response.write(output.getvalue())
    return response
