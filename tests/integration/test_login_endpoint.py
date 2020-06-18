# -*- coding: utf-8 -*-
# @Author: Aniket Maithani
# @Date:   2020-06-17 18:10:03
# @Last Modified by:   Aniket Maithani
# @Last Modified time: 2020-06-18 12:26:03
import json

import pytest

from .. import factories as f


@pytest.mark.django_db
def test_login_endpoint(client):
    url = '/api/v1/auth/token/login/'
    f.create_user(username='aniketmaithani', password="test123")
    login_creds = {
        "password": "test123",
        "username": "aniketmaithani"
    }
    response = client.json.post(url, json.dumps(login_creds))
    assert 'auth_token' in response.json()
    assert response.status_code == 200
