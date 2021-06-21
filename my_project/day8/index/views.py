from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *


# Create your views here.
def remark_views(request):
    if request.method == 'GET':
        form = RemarkForm()
        return render(request, 'remark.html', locals())
    else:
        # 接收提交的数据；将POST中的数据放在RemarkForm中。
        form = RemarkForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd['subject'])
            print(cd['mail'])
            print(cd['message'])
            print(cd['topic'])
            print(cd['issave'])
            # 此处可以将获取到的数据保存进数据库中。
            return HttpResponse('query ok!')
        else:
            return HttpResponse('error!')


def register_views(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'register.html', locals())
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # 将表单提交的数据和数库进行交互
            Users(**cd).save()
            return HttpResponse('register success!')
        else:
            return HttpResponse('error!')


def model_form_views(request):
    if request.method == 'GET':
        form = UsersForm()
        return render(request, 'model_form.html', locals())
    else:
        form = UsersForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Users(**cd).save()
            return HttpResponse('register ok!')
        else:
            return HttpResponse('error!')


def login_views(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', locals())
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            una = cd.get('uname', '')
            upw = cd.get('upwd', '')
            if una and upw:
                # 将表单提交的数据和数库进行交互
                users = Users.objects.filter(uname=una, upwd=upw)
                if users:
                    return HttpResponse('登录成功！')
                else:
                    errMsg = '用户名或密码不正确！'
                    return render(request, 'login.html', locals())


def widget1_views(request):
    form = WidgetForm()
    return render(request, "widget1.html", locals())
