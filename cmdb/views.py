# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response,RequestContext

from account.account_api import *
from account.models import *
from serversys.models import *
from cmdb.models import *

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
def cmdb_edit(request):
    if request.method == 'GET':
        Username = request.session.get('user_name')


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

