import factory
from factory import Faker, SubFactory
from Courses.factories import CourseFactory
from User.factories import UserFactory
from .models import ReviewsModel


class ReviewFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ReviewsModel

    course = SubFactory(CourseFactory)
    student = SubFactory(UserFactory, role='student')
    rating = Faker('random_int', min=1, max=5)
    review = Faker('text')
    created_at = Faker('date_time_this_year')
