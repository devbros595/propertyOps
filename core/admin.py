from django.contrib import admin
from .models import Service, Order, Payment, ContractorPayout


# Register your models here.
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
    )

    search_fields = ("name",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "service",
        "status",
        "assigned_contractor",
        "created_at",
    )

    list_filter = ("status",)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        "order",
        "amount",
        "paid",
    )

    list_filter = ("paid",)


@admin.register(ContractorPayout)
class ContractorPayoutAdmin(admin.ModelAdmin):
    list_display = (
        "contractor",
        "order",
        "amount",
        "paid",
    )

    list_filter = ("paid",)
