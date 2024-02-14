from django.contrib import admin

from santai.models import Order, CertificateOrder


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    date_hierarchy = 'updated_at'
    list_filter = ('is_permitted',)
    readonly_fields = ("updated_at",)
    list_display = ("phone", "name", "updated_at", "is_permitted",)


@admin.register(CertificateOrder)
class CertificateOrderAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    readonly_fields = ("created_at",)
    list_display = ("phone", "name", "massage", "time", "created_at",)
