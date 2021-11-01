from decimal import Decimal

import factory

from faker import Faker

from ..models import Pokemon

faker = Faker()


class PokemonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Pokemon

    poke_id = factory.sequence(lambda n: n)

    @factory.lazy_attribute
    def height(self):
        return Decimal(faker.numerify("###.##"))

    @factory.lazy_attribute
    def weight(self):
        return Decimal(faker.numerify("###.##"))
