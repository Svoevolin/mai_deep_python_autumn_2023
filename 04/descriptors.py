"""Module of descriptors for homework №2"""
import re


class Name:
    """Class of descriptor to validate person name"""

    def __get__(self, obj, objtype=None):
        return self.value

    def __set__(self, obj, value):

        if not isinstance(value, str):
            raise TypeError("Имя может содержать только буквы")

        if len(value) > 20:
            raise ValueError("Имя не может содержать больше 20 символов")

        self.value = value


class Email:
    """Class of descriptor to validate person email"""

    def __get__(self, obj, objtype=None):
        return self.value

    def __set__(self, obj, value):

        if not isinstance(value, str):
            raise TypeError("Почта может содержать только буквы")

        if not re.match(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', value):
            raise ValueError("Некорректный email")
        self.value = value


class Age:
    """Class of descriptor to validate person age"""
    def __get__(self, obj, objtype=None):
        return self.value

    def __set__(self, obj, value):

        if not isinstance(value, int):
            raise TypeError("Возраст это цифры")

        if value < 0 or value > 128:
            raise ValueError("Возраст не может быть отрицательным или больше 128")

        self.value = value


class Person:
    """Class using descriptors"""
    name = Name()
    email = Email()
    age = Age()

    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
