from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

# Register your models here.

class AccountAdmin(UserAdmin):
    #we decide which parametrs of user will be showed
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 
                    'date_joined','is_active')
    #links that we make clickable
    list_display_links = ('email', 'first_name', 'last_name')
    #read only(not clickable)
    readonly_fields = ('last_login', 'date_joined')
    #sorting by the parametr,'-' descending order(по-убыванию), without '-' ascending
    ordering = ('-date_joined',)

    #it makes pass read only
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)