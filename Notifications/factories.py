import factory
from factory import Faker, SubFactory
from User.factories import UserFactory
from .models import NotificationsModel


class NotificationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = NotificationsModel

    recipient = SubFactory(UserFactory)
    message = Faker('text')
    read = Faker('boolean')
    created_at = Faker('date_time_this_year')
