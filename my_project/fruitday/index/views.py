from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *


# Create your views here.
# def login_views(request):
#     if request.method == 'GET':
#         cookies = request.COOKIES
#         if 'id' in cookies and 'uphone' in cookies:
#             return HttpResponse('欢迎' + cookies['uphone'])
#         return render(request, 'login.html')
#     else:
#         uphone1 = request.POST.get('uphone', '')
#         upwd = request.POST.get('upwd', '')
#         # 1.登录验证方式1
#         # if uphone1 and upwd:
#         #     users = Users.objects.filter(uphone=uphone1,upass=upwd)
#         #     if users:
#         #         return HttpResponse('登录成功！')
#         #     else:
#         #         errMsg = '手机号或密码不正确！'
#         #         return render(request,'login.html',locals())

#         # 2.登录验证方式2
#         if uphone1 and upwd:
#             users = Users.objects.filter(uphone=uphone1)
#             if users:
#                 u = users[0]
#                 if upwd == u.upass:
#                     resp = HttpResponse('登录成功!')
#                     if 'isSaved' in request.POST:
#                         resp.set_cookie('id', u.id, 60 * 60 * 24 * 2)
#                         resp.set_cookie('uphone', u.uphone, 60 * 60 * 24 * 2)
#                         return resp
#                     else:
#                         return resp
#                 else:
#                     errMsg = '密码错误！'
#                     return render(request, 'login.html', locals())
#             else:
#                 errMsg = '对不起，手机号码不存在！'
#                 return render(request, 'login.html', locals())
#         else:
#             errMsg = '手机号或密码不能为空！'
#             return render(request, 'login.html', locals())


def login_views(request):
    if request.method == 'POST':
        uphone = request.POST.get('uphone', '')
        upwd = request.POST.get('upwd', '')
        uList = Users.objects.filter(uphone=uphone, upass=upwd)
        if uList:
            resp = HttpResponseRedirect('/index/')
            # 将手机号存进session
            request.session['uphone'] = uphone
            # 判断是否需要存进cookie
            if 'isSaved' in request.POST:
                resp.set_cookie('uphone', uphone, 60 * 60 * 24 * 30)
            return resp
        else:
            errMsg = '手机号或密码不正确！'
            return render(request, 'login.html', locals())
    else:
        # 判断是否处于已登录状态(session中是否有值)
        if 'uphone' in request.session:
            return HttpResponseRedirect('/index/')
        else:
            # 判断曾经是否登陆过(cookies中是否有值)
            if 'uphone' in request.COOKIES:
                uphone = request.COOKIES['uphone']
                request.session['uphone'] = uphone
                return HttpResponseRedirect('/index/')
            else:
                return render(request, 'login.html')


def register_views(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        uph = request.POST.get('uphone', '')
        upw = request.POST.get('upwd', '')
        una = request.POST.get('uname', '')
        uem = request.POST.get('uemail', '')
        if uph and upw and una and uem:
            # 先判断uphone数据是否存在？
            u = Users.objects.filter(uphone=uph)
            if u:
                errMsg = '手机号码已存在！'
                return render(request, 'register.html', locals())
            else:
                Users.objects.create(uphone=uph, upass=upw, uname=una, uemail=uem)
                return HttpResponse('注册成功！')
        else:
            return HttpResponse('数据不能为空！')


def index_views(request):
    return render(request, 'index.html')


def otm_views(request):
    goods = Goods.objects.get(id=1)
    goodsType = goods.goodsType
    gtype = GoodsType.objects.get(id=2)
    gds = gtype.goods_set.all()
    return render(request, 'otm.html', locals())
