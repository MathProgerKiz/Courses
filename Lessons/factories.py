import factory
from factory import Faker, SubFactory
from Courses.factories import CourseFactory
from .models import LessonsModel



class LessonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = LessonsModel

    title = Faker('word')
    description = Faker('text')
    course = SubFactory(CourseFactory)
    materials = Faker('url')
    order = Faker('random_int', min=1, max=1000)
