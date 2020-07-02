import pytest

@pytest.mark.django_db
def test_main(client):
    response = client.get('')
    assert response.status_code == 200

@pytest.mark.django_db
def test_login(client):
    response = client.get('/accounts/login/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_signup(client):
    response = client.get('/accounts/signup/')
    assert response.status_code == 200


# @pytest.mark.django_db
# def test_vehicles(client, user, transit):
#     response = client.get('/przewoz/vehicles/')
#     assert response.status_code == 200
#     assert len(response.context['objets']) == 1