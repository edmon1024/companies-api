import random
import requests
from datetime import date, timedelta
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
        stock_market = []
        current_date = date.today()
        ticker = validated_data.get("ticker","")
        ticker_validation = False

        r = requests.request(
            "POST",
            url="https://www.nyse.com/api/quotes/filter", 
            json={
                "instrumentType": "EQUITY",
                "pageNumber": 1,
                "sortColumn": "NORMALIZED_TICKER",
                "maxResultsPerPage": 10,
                "filterToken": ticker,
            }
        )
        res = r.json()

        if bool(res): 
            ticker_validation = True

        if ticker_validation == False:
            raise serializers.ValidationError({
                "ticker": _("The ticker structure is wrong")
            })


        for idx in range(50):
            stock_market_date = current_date - timedelta((50-idx))

            stock_market.append({
                "date": str(stock_market_date),
                "O":round(random.uniform(100, 500),2),
                "H":round(random.uniform(251, 500),2),
                "L":round(random.uniform(100, 250),2),
                "C":round(random.uniform(100, 500),2),
            })

        company = Company.objects.create(**validated_data, stock_market=stock_market)

        return company


    def update(self, instance, validated_data):
        instance.ticker = validated_data.get('ticker', instance.ticker)
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()

        return instance


