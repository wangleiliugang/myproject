from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.db.models import F, Q


# Create your views here.
def parent_views(request):
    return render(request, 'parent.html')


def child_views(request):
    return render(request, 'child.html')


# 1.增加数据操作
def add_author_views(request):
    # 1.使用Entry.objects.create()插入数据
    # Author.objects.create(name='小王',age=33,email='xiaowang@163.com')

    # 2.使用obj=Entry(属性＝'值') / obj.save()
    # obj = Author(name='小贾',age=35,email='xiaojia@163.com')
    # obj.save()

    # 3.使用字典完成对象的构建
    # dic = {
    #   'name':'小陈',
    #   'age':38,
    #   'email':'xiaochen@163.com',
    # }
    # obj = Author(**dic)
    # obj.save()
    # Author.objects.create(name='小武',age=29,email='xiaowu@163.com')
    return HttpResponse('add OK!')


def add_book_views(request):
    Book.objects.create(title='红楼梦', publication_date='1995-12-12')

    obj = Book(title='西游记', publication_date='1982-10-12')
    obj.save()

    dic = {
        'title': '三国演义',
        'publication_date': '1990-3-5',
    }
    obj = Book(**dic)
    obj.save()
    return HttpResponse('add Book OK!')


def add_publisher_views(request):
    Publisher.objects.create(name='中国人民出版社', address='五道口', city='北京', country='中国', website='http://www.renmin.com')

    obj = Publisher(name='中国动画片出版社', address='潘家园', city='北京', country='中国', website='http://www.renmin.com')
    obj.save()

    dic = {
        'name': '中国文玩出版社',
        'address': '昌平区',
        'city': '北京',
        'country': '中国',
        'website': 'http://www.wenwan.com',
    }
    obj = Publisher(**dic)
    obj.save()
    return HttpResponse('add Publisher OK!')


# 2.基本查询操作
def get_author_views(request):
    # 1.查询所有信息
    # authors = Author.objects.all()

    # 2.查询所有行的name列的值
    # authors = Author.objects.all().values('name')

    # 3.查询所有行的name,age列的值
    authors = Author.objects.all().values('name', 'age')

    # 4.查询id为3的作者的信息
    # auth = Author.objects.get(id=3, name='陈凡')

    # 5.查询age不是35的作者的信息
    # authors = Author.objects.exclude(age=35)

    # 6.查询所有信息并按照age降序排序
    # authors = Author.objects.order_by('-age')
    return render(request, 'show_authors.html', locals())


def author_list_views(request):
    authors = Author.objects.all()
    return render(request, 'author_list.html', locals())


def del_user_views(request, uid):
    Author.objects.get(id=uid).delete()
    return HttpResponseRedirect('/author_list/')


# # 3.修改操作
def update_author_views(request):
    # 1.修改单个实体对象
    auth = Author.objects.get(id=2)
    auth.name = '小亮'
    auth.email = 'xiaoliang@qq.com'
    auth.save()
    # 2.批量修改
    # Author.objects.all().update(age=50)

    # 跳转到author_list_views的视图上,以便实现模板的展现。(请求的转发)
    # return author_list_views(request)

    # 使用重定向的方式完成视图的跳转。(请求的重定向)
    return HttpResponseRedirect('/author_list/')


def doF_views(request):
    Author.objects.all().update(age=F('age') + 10)
    return HttpResponseRedirect('/author_list')


def doQ_views(request):
    authors = Author.objects.filter(Q(id=1) | Q(age__gt=45))
    return render(request, 'q.html', locals())


def raw_views(request):
    sql = "select * from author where email like '%%@163.com';"
    authors = Author.objects.raw(sql)
    return render(request, 'raw.html', locals())


# 查询所有的作者信息
def all_authors_views(request):
    authors = Author.objects.all()
    return render(request, 'all_authors.html', locals())


def oto_views(request):
    # 1.通过Wife找Author
    w = Wife.objects.get(id=1)
    a = w.auth
    # 2.反向查询，通过Author找Wife
    aa = Author.objects.get(name='开开')
    ww = aa.wife
    return render(request, 'oto.html', locals())


def otm_views(request):
    # 1.正向查询，通过Book查询Publisher
    book = Book.objects.get(id=1)
    pub = book.publisher11
    # 2.反向查询，通过Publisher查询Book
    pub = Publisher.objects.get(id=3)
    bookSet = pub.book_set.all()
    return render(request, 'otm.html', locals())


def mtm_views(request):
    # 1.在Author中查询Publisher
    author = Author.objects.get(id=3)
    pubList = author.publisher.all()
    # 2.在Publisher中查询Author
    pub = Publisher.objects.get(id=2)
    authorList = pub.author_set.all()
    return render(request, 'mtm.html', locals())


def book_author_views(request):
    book = Book.objects.get(id=3)
    auList = book.author.all()
    au = Author.objects.get(id=2)
    bookList = au.book_set.all()
    return render(request, 'bta.html', locals())


def name_count_views(request):
    count = Author.objects.name_count('小')
    aut = Author.objects.lt_age(42)
    # return HttpResponse(count)
    return HttpResponse(aut)
