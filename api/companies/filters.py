from django_filters import rest_framework as filters
from django.db.models import Q
from companies.models import Company


class CompanyFilter(filters.FilterSet):
    search = filters.CharFilter(method='search_filter',label="Search")
    sort = filters.OrderingFilter(
        fields=(
            ('ticker', 'ticker'),
            ('name', 'name'),
        ),

        field_labels={
            'ticker': 'Ticker',
            'name': 'name',
        }
    )

    class Meta:
        model = Company
        fields = ["search",]

    def search_filter(self, queryset, name, value):
        return queryset.filter(
            Q(name__icontains=value) |
            Q(description__icontains=value) |
            Q(ticker__icontains=value)
        )

