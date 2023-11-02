import re


class Name:
    def __get__(self, obj):
        return self.value

    def __set__(self, obj, value):

        if type(value) != str:
            raise TypeError("Имя может содержать только буквы")

        if len(value) > 20:
            raise ValueError("Имя не может содержать больше 20 символов")

        self.value = value


class Email:
    def __get__(self, obj):
        return self.value

    def __set__(self, obj, value):

        if type(value) != str:
            raise TypeError("Почта может содержать только буквы")

        if not re.match('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', value):
            raise ValueError("Некорректный email")
        self.value = value


class Age:
    def __get__(self, obj):
        return self.value

    def __set__(self, obj, value):

        if type(value) != int:
            raise TypeError("Возраст это цифры")

        if value < 0 or value > 128:
            raise ValueError("Возраст не может быть отрицательным или больше 128")

        self.value = value


class Person:

    name = Name()
    email = Email()
    age = Age()

    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
