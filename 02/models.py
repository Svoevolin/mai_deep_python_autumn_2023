"""Module only for dataclass model"""
from dataclasses import dataclass


@dataclass
class Person:
    """Dataclass for factory generating random json fields"""
    person_id: int
    name: str
    description: str
