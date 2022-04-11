from django.contrib import admin
from companies.models import (
    Company,
)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        "id","name","ticker",
        "created_at","updated_at",
    )
    fields = (
        "id","name","description","ticker",
        "stock_market","created_at","updated_at",
    )
    readonly_fields = ("id","created_at","updated_at",)
    search_fields = ("name","ticker","description",)


