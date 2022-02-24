from django.contrib import admin
from main import models

admin.site.site_header = 'Admin Dashboard'

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'department']
    list_filter = ('department',)

class AssetAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'totalstock']

class PossesionAdmin(admin.ModelAdmin):
    list_display = ['employee', 'product', 'fromdate']
    list_filter = ('employee', 'product',)
# Register your models here.
admin.site.register( models.Employee, EmployeeAdmin )
admin.site.register( models.Assets, AssetAdmin )
admin.site.register( models.Possesion, PossesionAdmin )