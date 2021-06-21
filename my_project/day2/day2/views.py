from django.http import HttpResponse


# 视图，处理用户的请求并给出响应
# request:表示用户的请求信息
# HttpResponse:响应给客户端的内容
def fun_views(request):
    return HttpResponse("hello Django")


def index_views(request):
    return HttpResponse('这是XX网站的首页！')


def fun_arg1_views(request, num):
    resp = HttpResponse('传递的参数值为：' + num)
    return resp


def get_url1_views(request, year, day, hour):
    resp = HttpResponse(year + ':' + day + ':' + hour)
    return resp


def get_url2_views(request, country, day):
    resp = HttpResponse(country + ':' + day)
    return resp


def show_views(request, name, age):
    resp = HttpResponse(name + ':' + age)
    return resp
