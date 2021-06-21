from django.contrib import admin
from .models import *


class UsersAdmin(admin.ModelAdmin):
    list_display = ('uname', 'uphone', 'uemail')
    list_editable = ('uphone',)
    fields = ('uphone', 'uemail', 'uname', 'isActive')
    search_fields = ('uname', 'uphone', 'uemail')


# Register your models here.
admin.site.register(Users, UsersAdmin)
admin.site.register(GoodsType)
admin.site.register(Goods)
