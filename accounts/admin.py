from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class AccocuntAdmin(UserAdmin):
    list_dispaly = ['email','first_name','last_name',"username",'last_login','is_active','date_joined']
    list_display_links = ("email",'first_name',"last_name")
    readonly_fields = ("last_login","date_joined")
    ordering = ("-date_joined",)
    list_filter = ()
    filter_horizontal = ()
    fieldsets = ()




admin.site.register(Account,AccocuntAdmin)
