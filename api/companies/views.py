from rest_framework import viewsets
from .models import Company
from .serializers import (
    CompanyListSerializer,
    CompanyRetrieveSerializer,
)
from .filters import CompanyFilter



class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanyRetrieveSerializer
    filter_class = CompanyFilter

    def get_serializer_class(self):
        if self.action == "list":
            return CompanyListSerializer

        return self.serializer_class


