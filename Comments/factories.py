import factory
from factory.django import DjangoModelFactory
from .models import UsersModel


class UserFactory(DjangoModelFactory):
    """Класс для того чтобы генерировать различные данные для юзера"""
    class Meta:
        model = UsersModel

    username = factory.Faker("user_name")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Faker("email")
    is_staff = True
