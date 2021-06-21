from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index_views(request):
    resp = HttpResponse('<h1>这是news的首页</h1>')
    return resp


def first_views(request):
    return render(request, 'first.html')


def second_views(request):
    return render(request, 'second.html')


def show_views(request, num):
    return HttpResponse("传递进来的参数为:" + num)


def result_views(request, num1, num2):
    r = int(num1) + int(num2)
    return HttpResponse("Result is %d" % r)


def var_views(request):
    lis = ['张三丰', '张无忌', '张翠山']
    tup = ('赵敏', '殷素素', '周芷若')
    dic = {'a': 'ABC', 'b': 'BEYOND'}

    dic1 = {
        'num': 25,
        'str': 'Hello Django',
        'list': lis,
        'tup': tup,
        'dic': dic,
        'fun': fun(25, 12),
        'A': A()
    }
    return render(request, 'var.html', dic1)


def fun(a, b):
    return a + b


class A(object):
    def fun(self):
        return "A -> f()"
