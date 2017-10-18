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
        Supplier = Group_Supplier.objects.all()

        kwvars = {
            'request':request,
            'Username': Username,
            'Deptdata': Deptdata,
            'Supplier': Supplier,
        }

        return render_to_response('cmdb/cmdb_add.html',kwvars,RequestContext(request))

