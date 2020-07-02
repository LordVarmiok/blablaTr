# import pytest
# from django.contrib.auth.models import User
#
# from przewoz.models import Vehicle, Cargo, Transit
#
#
# @pytest.fixture
# def user():
#     user = User(
#         first_name='piotr',
#         last_name='lee',
#         email='piotr@mail.net',
#         username='piotrlee',
#     )
#     user.set_password = 'pol123321'
#     user.save()
#     return user
#
#
# @pytest.fixture
# def vehicle():
#     g = [Vehicle.objects.create(
#         brand='Mercedes',
#         type='tir',
#         driver=user(),
#         volume=5,
#         max_capacity=5,
#         max_length=5,
#         description='test'
#     )]
#     return g


# @pytest.fixture
# def transit(vehicle):
#     t = [Transit.objects.create(
#         vehicle=vehicle,
#         driver='user',
#         # departure='A',
#         # arrival='b',
#         destination='A',
#         place_of_departure='b',
#         description='test'
#     )]
#     return t