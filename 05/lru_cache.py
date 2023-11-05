from weakref import WeakValueDictionary
from double_link_list import Node, DoubleLinkedList


class LRUCache:

    def __init__(self, max_size):
        self.dict = WeakValueDictionary()
        self.order_list = DoubleLinkedList()
        self.current_size = 0
        self.max_size = max_size

    def __len__(self):
        return len(self.dict)

    def __getitem__(self, key):
        if (el := self.dict.get(f'{key}')) is not None:
            self.order_list.remove(el)
            self.order_list.append(el)
            return el.value
        else:
            raise KeyError(f'Key "{key}" unfounded')

    def __setitem__(self, key, value):
        if (el := self.dict.get(f'{key}')) is not None:
            self.order_list.remove(el)
            self.current_size -= 1

        elif self.current_size == self.max_size:
            self.order_list.remove(self.order_list.get_head())
            self.current_size -= 1

        new_el = Node(value)
        self.order_list.append(new_el)
        self.dict[key] = new_el
        self.current_size += 1

    def __del__(self):
        while self.order_list.get_head():
            self.order_list.remove(self.order_list.get_head())
