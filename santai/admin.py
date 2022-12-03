from django.contrib import admin

from santai.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    date_hierarchy = 'updated_at'
    list_filter = ('is_permitted',)
    readonly_fields = ("updated_at",)
