#!/usr/bin/python3
"""linked list"""


class Node:
    """Node for linked list"""
    def __init__(self, data, next_node=None):
        """init node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """access data"""
        return self.__data

    @data.setter
    def data(self, value):
        """set data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """access next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """set next node"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """list class"""
    def __init__(self):
        """init list"""
        self.__head = None

    def __str__(self):
        """to string"""
        node = self.__head
        result = []
        while node is not None:
            result.append(str(node.data))
            node = node.next_node
        return "\n".join(result)

    def sorted_insert(self, value):
        """insert in sorted order"""
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        elif value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            node = self.__head
            while node.next_node is not None and node.next_node.data < value:
                node = node.next_node
            new_node.next_node = node.next_node
            node.next_node = new_node
