import factory
from factory import Faker, SubFactory
from Assignments.factories import AssignmentFactory
from User.factories import UserFactory
from .models import SubmissionsModel


class SubmissionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = SubmissionsModel

    student = SubFactory(UserFactory, role='student')
    assignment = SubFactory(AssignmentFactory)
    response = Faker('text')
    status = Faker('word', ext_word_list=['checked', 'unchecked'])
    grade = Faker('random_int', min=0, max=100)
    comments = Faker('text')
    submission_date = Faker('date_time_this_year')
