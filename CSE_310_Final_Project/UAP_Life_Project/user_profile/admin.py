from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin
from .models import Promo


class AccountAdmin(UserAdmin):
    list_display = ('email', 'username','first_name','last_name','date_joined','is_admin','is_staff')
    search_field = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)
admin.site.register(Promo)