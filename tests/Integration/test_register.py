import pytest
from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework.test import APIClient


client = APIClient()

#aaaaa


@pytest.mark.django_db
def test_login():
    payload = dict(
        name="motaz",
        email="motaz123@abc.com",
        password="991594123rami"
    )
    response = client.post('/api/users/register/', payload)
    response=client.post('/api/users/login/',dict(username="motaz123@abc.com",password="991594123rami"))
    print(response.data)
    assert response.status_code==200




