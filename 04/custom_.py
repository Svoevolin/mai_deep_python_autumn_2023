class CustomMeta(type):
    def __new__(mcs, name, bases, classdict, **kwargs):

        attrs = []
        for key in classdict:
            if not key.startswith("__"):
                attrs.append(key)

        for attr in attrs:
            classdict[f'custom_{attr}'] = classdict[attr]
            del classdict[attr]

        def __setattr__(self, attr_name, attr_value):
            if not attr_name.startswith("__"):
                attr_name = f'custom_{attr_name}'
            object.__setattr__(self, attr_name, attr_value)

        classdict['__setattr__'] = __setattr__

        return super().__new__(mcs, name, bases, classdict, **kwargs)


class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100

    def __str__(self):
        return "Custom_by_metaclass"
