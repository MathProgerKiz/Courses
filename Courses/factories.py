import factory
from factory import Faker, SubFactory
from User.factories import UserFactory
from .models import CoursesModel



class CourseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CoursesModel

    title = Faker('word')
    description = Faker('text')
    instructor = SubFactory(UserFactory, role='instructor')
    created_at = Faker('date_time_this_decade')
