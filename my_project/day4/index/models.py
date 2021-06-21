from django.db import models
import datetime


class AuthorManager(models.Manager):
    # 1.自定义查找Author中包含指定关键字的书籍的数量
    def name_count(self, keywords):
        return self.filter(name__contains=keywords).count()

    # 2.自定义年纪小于指定年纪的所有作者的信息
    def lt_age(self, tar):
        return self.filter(age__lt=tar)


# Create your models here.
# 实体类：Publisher
# 对应到数据库中的一张表
# 该类中的每个属性，会对应到数据库中表的每个字段
class Publisher(models.Model):
    name = models.CharField(max_length=30, default='匿名', verbose_name='名称')
    address = models.CharField(max_length=50, verbose_name='地址')
    city = models.CharField(max_length=20, verbose_name='所在城市')
    country = models.CharField(max_length=20, verbose_name='国家')
    website = models.URLField(verbose_name='网址')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'publisher'
        verbose_name = '出版社'
        verbose_name_plural = verbose_name


class Author(models.Model):
    # 重新指定objects类
    objects = AuthorManager()

    name = models.CharField(max_length=30, verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')
    email = models.EmailField(null=True, verbose_name='邮箱')
    picture = models.ImageField(null=True, upload_to='static/upload/usrimg', verbose_name='用户图像')
    # 创建多对多关系，Author(M):Publisher(N)
    publisher = models.ManyToManyField(Publisher, verbose_name='签约出版社')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'author'
        verbose_name = '作者'
        verbose_name_plural = verbose_name
        ordering = ['-age', 'id']


class Book(models.Model):
    title = models.CharField(max_length=50, verbose_name='书名')
    publication_date = models.DateField(verbose_name='出版日期')
    # 增加1:M的映射，引用Publisher
    publisher11 = models.ForeignKey(Publisher, null=True, verbose_name='出版社')
    author = models.ManyToManyField(Author, verbose_name='作者')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'book'
        verbose_name_plural = '书籍'
        ordering = ['-publication_date']


class Wife(models.Model):
    name = models.CharField(max_length=30, verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')
    # 增加1:1的映射，引用Author
    auth = models.OneToOneField(Author, null=True, verbose_name='先生')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'wife'
        verbose_name = '女士'
        verbose_name_plural = verbose_name
