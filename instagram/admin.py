from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from instagram.models import MyUser


# Register your models here.

class MyUserAdmin(BaseUserAdmin):
    list_display=('email', 'company_name','date_joined','last_login','is_admin','is_active')
    search_fields=('email', 'company_name')
    readonly_fields=('date_joined','last_login')
    filter_horizontal=()
    last_filter=('last_login',)
    fieldsets=()

    add_fieldsets=(
        (None,{
            'classes':('wide'),
            'fields':('email', 'company_name', 'phone', 'password1', 'password2'),
        }),
    )

    ordering=('email',)


admin.site.register(MyUser)