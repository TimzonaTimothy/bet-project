from django.contrib import admin
from .models import *
# Register your models here.

class DepositAdmin(admin.ModelAdmin):
    list_display = ('user','amount','ref')
    list_display_links = ('user','amount')
    search_fields = ('user','ref')
    list_per_page = 25
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Deposit, DepositAdmin)