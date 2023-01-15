from django.contrib import admin
from web_app.models import *
# Register your models here.
admin.site.site_header = '後臺管理'
admin.site.site_title  = '後臺管理'

class SyUserAdmin(admin.ModelAdmin):
    list_display = ('syid', 'username', 'area', 'workunit')

admin.site.register(SyUser,SyUserAdmin)
admin.site.register(UserArea)
admin.site.register(UserUnit)
admin.site.register(AssetBasic)
admin.site.register(AssetMove)