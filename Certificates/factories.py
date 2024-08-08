import factory
from factory import Faker, SubFactory
from Courses.factories import CourseFactory
from User.factories import UserFactory
from .models import CertificatesModel


class CertificateFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CertificatesModel

    student = SubFactory(UserFactory, role='student')
    course = SubFactory(CourseFactory)
    issued_date = Faker('date_time_this_year')
    status = Faker('word', ext_word_list=['issued', 'not issued'])
