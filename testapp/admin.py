from django.contrib import admin
from testapp.models import UsersTable
# Register your models here.
class UsersTableAdmin(admin.ModelAdmin):
    list_display=['email','password']
admin.site.register(UsersTable,UsersTableAdmin)
