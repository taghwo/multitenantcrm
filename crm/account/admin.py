from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from account.models import Account


@admin.register(Account)
class AccountAdmin(UserAdmin):
    list_display = ('email', 'fullname')
