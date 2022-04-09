from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _

from .models import (
    Company,
)


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = (
            'id','name','description','symbol','market_values',
            'created_at','updated_at',
        )
        read_only_fields = ('id','created_at','updated_at',)


