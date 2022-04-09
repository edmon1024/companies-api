from django.utils import timezone
import datetime
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import get_object_or_404
from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import (
    Company,
)
from .serializers import (
    CompanySerializer,
)
from .filters import CompanyFilter



class CompanyViewSet(mixins.ListModelMixin, 
                      mixins.CreateModelMixin,
                      viewsets.GenericViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_class = CompanyFilter

    def get_serializer_class(self):
        if self.action == "create":
            return CompanySerializer

        return self.serializer_class


