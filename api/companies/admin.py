from django.contrib import admin
from companies.models import (
    Company,
)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        "id","name","symbol",
        "created_at","updated_at",
    )
    fields = (
        "id","name","description","symbol",
        "market_values","created_at","updated_at",
    )
    readonly_fields = ("id","created_at","updated_at",)
    search_fields = ("name","symbol",)


