from django_filters import rest_framework as filters
from companies.models import Company


class CompanyFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr="icontain")
    description = filters.CharFilter(lookup_expr="icontain")
    symbol = filters.CharFilter(lookup_expr="icontain")

    class Meta:
        model = Company
        fields = ["name","description","symbol",]
