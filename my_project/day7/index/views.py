from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.
def show_request_views(request):
    # print(dir(request))
    scheme = request.scheme
    body = request.body
    path = request.path
    host = request.get_host()
    method = request.method
    get = request.GET
    post = request.POST
    cookie = request.COOKIES
    meta = request.META
    return render(request, 'show_request.html', locals())


def show_get_views(request):
    # 获取get请求提交的数据
    get = request.GET
    # name = request.GET['name']
    # age = request.GET['age']
    if 'name' in request.GET:
        name = request.GET['name']
    if 'age' in request.GET:
        age = request.GET['age']
    return render(request, 'show_get.html', locals())


def login_views(request):
    # 判断是post请求还是get请求，来分析用户的意图
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        return HttpResponse('处理数据!')


def register_views(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        if 'uname' in request.POST:
            un = request.POST['uname']
        if 'upwd' in request.POST:
            up = request.POST['upwd']
        if 'uemail' in request.POST:
            ue = request.POST['uemail']
    Users.objects.create(uname=un, upass=up, uemail=ue)
    return HttpResponse('Register OK!')
