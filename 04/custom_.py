"""Module of metaclass for homework №1"""


class CustomMeta(type):
    """So it's metaclass"""
    def __new__(mcs, name, bases, classdict, **kwargs):

        attrs = []
        for key in classdict:
            if not key.startswith("__"):
                attrs.append(key)

        for attr in attrs:
            classdict[f'custom_{attr}'] = classdict[attr]
            del classdict[attr]

        def __setattr__(self, attr_name, attr_value):
            object.__setattr__(
                self,
                attr_name if attr_name.startswith("__") else f'custom_{attr_name}',
                attr_value
            )

        classdict['__setattr__'] = __setattr__

        return super().__new__(mcs, name, bases, classdict, **kwargs)


class CustomClass(metaclass=CustomMeta):
    """Class with self variable, method, magic method and dynamic variable in init"""
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        """method to rename"""
        return 100

    def __str__(self):
        """method to keep name"""
        return "Custom_by_metaclass"
