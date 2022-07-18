# import pytest
# from rest_framework.test import APIClient
#
# client=APIClient()
#
# @pytest.mark.django_db
# def test_login_user():
#     payload = dict(
#         name="toti",
#         email="toti_kk@gmail",
#         password="totikk"
#     )
#     client.post("/api/users/register/", payload)
#     response = client.post("/api/users/login/", dict(username="toti_kk@gmail",password="totikk"))
#     data = response.data
#     assert data["username"] == payload["email"]
#     assert "password" not in data
#     assert response.status_code == 200 # status 200 for login success
