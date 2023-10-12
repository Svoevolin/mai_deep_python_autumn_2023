"""Module with factory to generate fake json objects"""
import factory
from models import Person


class PersonFactory(factory.Factory):
    """Factory to generate fake json objects"""
    class Meta:
        """Helper class"""
        model = Person

    person_id = factory.Faker('pyint', min_value=1000, max_value=10000000)
    name = factory.Faker('name')
    description = factory.Faker('sentence', nb_words=30)
