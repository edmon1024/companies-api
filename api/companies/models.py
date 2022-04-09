from django.db import models
from django.utils.translation import ugettext_lazy as _
from .abstract_models import (
    AbstractCreatedUpdatedAt,
)
from .utils.utils import hex_uuid


class Company(AbstractCreatedUpdatedAt):
    id = models.UUIDField(
        primary_key=True, 
        default=hex_uuid,
        editable=False, 
        unique=True,
    )
    name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name=_("Name"),
    )
    description = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name=_("Description"),
    )
    symbol = models.CharField(
        max_length=10,
        null=False,
        blank=False,
        verbose_name=_("Symbol"),
    )
    market_values = models.JSONField(
        verbose_name=_("Market values"),
        default=list,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Company")
        verbose_name_plural = _("Companies")


