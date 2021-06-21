from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index_views(request):
    resp = HttpResponse('<h1>这是sport的首页</h1>')
    return resp


def person_views(request):
    uname = 'SanFeng.Zhang'
    uage = 15
    ugender = 1
    uhobby = ['打太极', '爬山', '舞剑']
    # 使用locals()封装局部变量数据到一个字典中去，
    # 传递函数和对象时不能用此函数，需要自己写.
    return render(request, 'person.html', locals())
