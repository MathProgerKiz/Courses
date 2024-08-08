import factory
from factory import Faker, SubFactory
from Lessons.factories import LessonFactory
from Assignments.factories import AssignmentFactory
from Submissions.factories import SubmissionFactory
from User.factories import UserFactory
from .models import CommentsModel


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CommentsModel

 
    author = SubFactory(UserFactory)
    content = Faker('text')
    created_at = Faker('date_time_this_year')
    lesson = SubFactory(LessonFactory, nullable=True)
    assignment = SubFactory(AssignmentFactory, nullable=True)
    response = SubFactory(SubmissionFactory, nullable=True)
