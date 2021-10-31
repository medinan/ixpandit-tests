import factory
from django.contrib.auth import get_user_model

from faker import Faker

faker = Faker()

user_model = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = user_model

    username = factory.sequence(lambda n: f"username_{n}")
