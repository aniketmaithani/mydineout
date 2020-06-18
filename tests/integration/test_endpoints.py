# -*- coding: utf-8 -*-
# @Author: Aniket Maithani
# @Date:   2020-06-17 19:08:31
# @Last Modified by:   Aniket Maithani
# @Last Modified time: 2020-06-18 09:16:33
import pytest


@pytest.mark.django_db
def test_endpoints_without_authorization(client):
    url_list = ['/api/v1/restaurant/getrestaurant',
                '/api/v1/restaurant/fromdistance',
                '/api/v1/restaurant/blacklistrestaurant',
                '/api/v1/restaurant/favouriterestaurant']
    for url in url_list:
        data = {}
        response = client.json.post(url, data)
        assert response.status_code == 401  # requires authorization
