from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

import json

from rest_framework.test import APIClient
from rest_framework import status

from companies.models import (
    Company,
)


class CompanyTestCase(TestCase):
    def setUp(self):
        user = User(
            email="edmon.af@gmail.com",
            first_name="Edmundo",
            last_name="Andrade",
            username="eandrade",
        )
        user.set_password("1234567890***")
        user.save()

        self._client = self._get_client()

        self.now = timezone.now()

    def _get_token(self):
        client = APIClient()

        response = client.post(
            "/api/v1/auth/", {
                "username": "eandrade",
                "password": "1234567890***"
            },
        )

        result = json.loads(response.content)

        return result["token"]

    def _get_client(self):
        token = self._get_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION="Token "+ token)
    
        return client
        

