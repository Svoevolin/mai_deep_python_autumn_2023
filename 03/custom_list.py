"""Module only for class of custom list"""
from typing import List
from itertools import zip_longest
from functools import partial

fill_zero = partial(zip_longest, fillvalue=0)


class CustomList(List):
    """Class of CustomList"""

    def __add__(self, other):
        return CustomList([f+s for f, s in fill_zero(self, other)])

    def __radd__(self, other):
        return CustomList([f+s for f, s in fill_zero(self, other)])

    def __sub__(self, other):
        return CustomList([f-s for f, s in fill_zero(self, other)])

    def __rsub__(self, other):
        return CustomList([f-s for s, f in fill_zero(self, other)])

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __ne__(self, other):
        return sum(self) != sum(other)

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __str__(self):
        return f'{str(list(self))}, sum = {len(self)}'
