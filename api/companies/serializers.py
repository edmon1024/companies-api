import random
from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _

from .models import (
    Company,
)


class CompanyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = (
            'id','ticker','name','description',
            'created_at','updated_at',
        )
        read_only_fields = ('id','created_at','updated_at',)


class CompanyRetrieveSerializer(CompanyListSerializer):
    ticker = serializers.CharField(required=True, min_length=1, max_length=10)
    name = serializers.CharField(required=True, min_length=1, max_length=50)
    description = serializers.CharField(required=True, min_length=1, max_length=100)

    class Meta:
        model = Company
        fields = (
            'id','ticker','name','description',
            'stock_market','created_at','updated_at',
        )
        read_only_fields = ('id','stock_market','created_at','updated_at',)

    def create(self, validated_data):
        stock_market = [round(random.uniform(100, 500),2) for idx in range(49)]
        company = Company.objects.create(**validated_data, stock_market=stock_market)

        return company


    def update(self, instance, validated_data):
        instance.ticker = validated_data.get('ticker', instance.ticker)
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()

        return instance


