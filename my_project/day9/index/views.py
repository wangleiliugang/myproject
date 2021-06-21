from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
def add_cookie1_views(request):
    resp = HttpResponse("请求成功，数据保存进cookie")
    resp.set_cookie("uname", "zsf", 60 * 60 * 24 * 2)
    return resp


def get_cookie1_views(request):
    # print(request.COOKIES)
    if 'uname' in request.COOKIES:
        return HttpResponse(request.COOKIES['uname'])
    return HttpResponse("获取cookies信息： %s" % request.COOKIES)


def add_session_views(request):
    request.session['uname'] = 'sf.zhang'
    request.session.set_expiry(0)
    return HttpResponse('Add Session OK!')


def get_session_views(request):
    if 'uname' in request.session:
        uname = request.session.get('uname')
        return HttpResponse('欢迎' + uname)
    return HttpResponse('对不起！未获取到数据...')


def login_views(request):
    if request.method == 'GET':
        uname = request.session.get('uname', '')
        return render(request, 'login.html', locals())
    else:
        uname = request.POST.get('uname', '')
        upwd = request.POST.get('upwd', '')
        if uname and upwd:
            if uname == 'zsf' and upwd == 'yss':
                request.session['uname'] = uname
                return HttpResponseRedirect('/index/')
            else:
                return HttpResponse('用户名或密码错误！')
        else:
            return HttpResponse('用户名或密码不能为空！')


def index_views(request):
    if 'uname' in request.session:
        uname = request.session.get('uname')
        return HttpResponse('欢迎' + uname + '来到首页！')
    else:
        return HttpResponse('欢迎！！！')


def log_out_views(request):
    del request.session['uname']
    return HttpResponseRedirect('/login/')
