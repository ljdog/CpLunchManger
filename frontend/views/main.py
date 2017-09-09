#encoding:utf-8

from django.http import HttpResponse, HttpResponseRedirect

def hellow(request):
    return HttpResponse("hell")
    return render_to_response('UserManage/role.add.html', kwvars, RequestContext(request))
