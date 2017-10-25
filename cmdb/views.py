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
        fan = request.POST.get('fan')
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

        p=cmdb(Cpu=cpu,Fan=fan,Motherboard=motherboard,Memory=memory,Graphics=graphics,Hard_disk1=hard_disk1,Keyboard=keyboard,
               Chassis=chassis,Power_Supply=power_supply,Monitor=monitor,Who_uses=who_uses,Price=price,Supplier=supplier,dept=deptname,comment=description,Create_Date=datetime)
        p.save()
        return HttpResponse(u'添加成功')

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

        print "----->",type(request.POST),request.POST['supplier_name']
        Getsupp_name = request.POST.get('supplier_name')
        # Getsupp_phone = request.POST.get('supplier_phone')

        print Getsupp_name

        # if group_supplier.objects.filter(id=sid,supplier_name=Getsupp_name,phone=Getsupp_phone):
        #     Getsupp = group_supplier.objects.get(id=sid)
        #     Getsupp.supplier_name = request.POST.get('supplier_name')
        #     Getsupp.phone = request.POST.get('supplier_phone')
        #     Getsupp.save()
        #     return HttpResponse(u"供应商修改成功!!!")
        #
        # if group_supplier.objects.filter(supplier_name=Getsupp_name,phone=Getsupp_phone):
        #     return HttpResponse(u'供应商已经存在，请重新输入')
        # else:
        #     Getsupp = group_supplier.objects.get(id=sid,supplier_name=Getsupp_name,phone=Getsupp_phone)
        #     Getsupp.supplier_name = request.POST.get('supplier_name')
        #     Getsupp.phone = request.POST.get('supplier_phone')
        #     Getsupp.save()
        #     return HttpResponse(u"供应商修改成功!!!")

        return HttpResponse(u'ok')

    # if request.method == 'POST':
    #     GetDeptname=request.POST.get('dept_name')
    #
    #     if Dept.objects.filter(name=GetDeptname,id=deid):
    #
    #         GetDept=Dept.objects.get(id=deid)
    #         GetDept.name=request.POST.get('dept_name')
    #         GetDept.save()
    #         return HttpResponse(u"部门修改成功!!!")
    #
    #     if Dept.objects.filter(name=GetDeptname):
    #         return HttpResponse(u"部门已经存在，请重新输入!!!")
    #     else:
    #         GetDept=Dept.objects.get(id=deid)
    #         GetDept.name=request.POST.get('dept_name')
    #         GetDept.save()
    #         return HttpResponse(u"部门修改成功!!!")
