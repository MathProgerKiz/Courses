import factory
from factory import Faker, SubFactory
from Lessons.factories import LessonFactory
from .models import AssignmentsModel



class AssignmentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AssignmentsModel

    title = Faker('word')
    description = Faker('text')
    lesson = SubFactory(LessonFactory)
    due_date = Faker('date_time_this_year')
