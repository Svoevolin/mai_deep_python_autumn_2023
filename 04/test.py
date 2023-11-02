"""Module for test"""
import unittest
from custom_ import CustomClass
from descriptors import Person


class TestMetaclass(unittest.TestCase):
    """Test metaclass(the first exercise)"""

    def test_static_variable_1(self):
        """Test static variable renamed to custom_{name}"""
        custom = CustomClass()
        self.assertEqual(custom.custom_x, 50)

    def test_static_variable_2(self):
        """Test static variable renamed to custom_{name}"""
        custom = CustomClass()
        with self.assertRaises(AttributeError):
            something = custom.x

    def test_method(self):
        """Test method renamed to custom_{name}"""
        custom = CustomClass()
        self.assertEqual(custom.custom_line(), 100)

    def test_method_2(self):
        """Test method renamed to custom_{name}"""
        custom = CustomClass()
        with self.assertRaises(AttributeError):
            custom.line()

    def test_dynamic_variable_1(self):
        """Test dynamic variable renamed to custom_{name}"""
        custom = CustomClass()
        custom.dynamic_variable = 999
        self.assertEqual(custom.custom_dynamic_variable, 999)

    def test_dynamic_variable_2(self):
        """Test dynamic variable renamed to custom_{name}"""
        custom = CustomClass()
        custom.dynamic_variable = 999
        with self.assertRaises(AttributeError):
            something = custom.dynamic_variable


class TestDescriptors(unittest.TestCase):
    """Test descriptors(the second exercise)"""

    def test_good_name(self):
        """Test set good name and get this"""
        person = Person(name='Ваня', email='mai@mai.ru', age=15)
        self.assertEqual(person.name, 'Ваня')

    def test_bad_name_1(self):
        """Test set bad name (uncorrected value)"""
        with self.assertRaises(TypeError):
            Person(name=81237, email='mai@mai.ru', age=15)

    def test_bad_name_2(self):
        """Test set bad name (too long)"""
        with self.assertRaises(ValueError):
            Person(name='qwertqwertqwertqwerty', email='mai@mai.ru', age=15)

    def test_good_email(self):
        """Test set good email and get this"""
        person = Person(name='Ваня', email='mai@mai.ru', age=15)
        self.assertEqual(person.email, 'mai@mai.ru')

    def test_bad_email_1(self):
        """Test set bad email (bad by type)"""
        with self.assertRaises(TypeError):
            Person(name='Ваня', email=15, age=15)

    def test_bad_email_2(self):
        """Test set bad email (bad by format)"""
        with self.assertRaises(ValueError):
            Person(name='Ваня', email='mai@mai', age=15)

    def test_good_age(self):
        """Test set good age and get this"""
        person = Person(name='Ваня', email='mai@mai.ru', age=15)
        self.assertEqual(person.age, 15)

    def test_bad_age_1(self):
        """Test set bad age (bad by type)"""
        with self.assertRaises(TypeError):
            Person(name='Ваня', email='mai@mai.ru', age='15')

    def test_bad_age_2(self):
        """Test set bad age (bad by value)"""
        with self.assertRaises(ValueError):
            Person(name='Ваня', email='mai@mai', age=-15)
