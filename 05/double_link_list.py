class Node:

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class DoubleLinkedList:

    head = None
    tail = None

    def is_empty(self):
        return self.head is None

    def get_head(self):
        return self.head

    def append(self, node):

        node.left, node.right = self.tail, None

        if self.head is None:
            self.head = node

        if self.tail is not None:
            self.tail.right = node

        self.tail = node

    def remove(self, node):
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
