from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CompaniesConfig(AppConfig):
    name = 'companies'
    verbose_name = _("Company")
    verbose_name_plural = _("Companies")

