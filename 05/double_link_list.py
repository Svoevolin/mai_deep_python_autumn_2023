"""Module of double linked list for ordering in the LRU cache"""
from dataclasses import dataclass


@dataclass
class Node:  # pylint: disable=too-few-public-methods
    """Class of element of double linked list"""
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class DoubleLinkedList:
    """Double linked list class"""

    head = None
    tail = None

    def is_empty(self):
        """Checking for empty list in O(1)"""
        return self.head is None

    def get_head(self):
        """Getting the head of a list in O(1)"""
        return self.head

    def append(self, node):
        """Appending a node to the tail in O(1)"""

        node.left, node.right = self.tail, None

        if self.head is None:
            self.head = node

        if self.tail is not None:
            self.tail.right = node

        self.tail = node

    def remove(self, node):
        """Removing an element from anywhere in O(1)"""

        left, right = node.left, node.right

        if left:
            left.right = right

        elif self.head == node:
            self.head = right

        if right:
            right.left = left

        elif self.tail == node:
            self.tail = left

        node.left, node.right = None, None
