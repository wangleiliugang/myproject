from django.shortcuts import render
from django.http import HttpResponse
# 1.导入loader
from django.template import loader


# Create your views here.
def index_views(request):
    resp = HttpResponse('<h1>这是music的首页!</h1>')
    return resp


def show_views(request):
    # 1.通过loader获取模板
    t = loader.get_template('show.html')
    # 2.将模板转换为字符串
    html = t.render({'title': 'Django模板'})
    # 3.再将字符串通过HttpResponse进行响应
    return HttpResponse(html)


def music_info_views(request):
    # t = loader.get_template('music_info.html')
    # dict1 = {
    #      'mName':'小苹果',
    #      'author':'筷子兄弟',
    #      'player':'筷子兄弟',
    # }
    # html = t.render(dict1)
    # return HttpResponse(html)

    dict1 = {
        'mName': '大鸭梨',
        'author': '烤鸭兄弟',
        'player': '筷子兄弟',
    }
    return render(request, 'music_info.html', dict1)
