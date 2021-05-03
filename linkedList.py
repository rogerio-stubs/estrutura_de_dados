from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def __len__(self):
        return self._size

    def __repr__(self):
        return '[' + str(self.head) + ']'

    def __str__(self):
        return self.__repr__()

    def __getitem__(self, index):
        pointer = self._get_node(index)
        if pointer:
            return pointer.data
        raise IndexError('list index out of range')

    def __setitem__(self, index, elem):
        pointer = self._get_node(index)

        if pointer:
            pointer.data = elem
        else:
            raise IndexError('list index out of range')

    def _get_node(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError('list index out of range')
        return pointer

    def append(self, elem):
        if self.head:
            poniter = self.head
            while(poniter.next):
                poniter = poniter.next
            poniter.next = Node(elem)
        else:
            self.head = Node(elem)
        self._size += 1

    def index(self, elem):
        pointer = self.head
        idx = 0
        while(pointer):
            if pointer.data == elem:
                return idx
            else:
                pointer = pointer.next
                idx += 1
        raise ValueError('{} is not in list'.format(elem))

    def insert(self, index, elem):
        node = Node(elem)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            pointer = self._get_node(index-1)
            node.next = pointer.next
            pointer.next = node
        self._size += 1

    def remove(self, elem):
        if self.head == None:
            raise ValueError('{} is not in list'.format(elem))
        elif self.head.data == elem:
            self.head = self.head.next
            self._size -= 1
            return True
        else:
            ancestor = self.head
            pointer = self.head.next
            while(pointer):
                if pointer.data == elem:
                    ancestor.next = pointer.next
                    pointer.next = None
                ancestor = pointer
                pointer = pointer.next
            self._size -= 1
            return True
        raise ValueError('{} is not in list'.format(elem))
        
