from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# 声明一个视图处理函数，login_views
def login_views(request):
    return HttpResponse('Here is index login')
