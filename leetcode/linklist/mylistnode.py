#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author    : Young
@Email     : hyc554@outlook.com
@site      : http://www.cnblogs.com/huang-yc/
@File      : mylistnode.py
@version   : 1.0
@Time      : 2019/4/2 21:53
Description about this file:

"""


class Node:
    def __init__(self, value, next_=None):
        self.val = value
        self.next = next_


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._head = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """

        new_node = self._head
        for i in range(index):
            if new_node.next is None:
                raise IndexError("越界")

            new_node = new_node.next
        return new_node.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self._head = Node(value=val, next_=self._head)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        current_node = self._head
        while current_node.next is not None:
            current_node = current_node.next
        new_tail = Node(value=val, next_=None)
        current_node.next = new_tail

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        pre_node = None
        current_node = self._head
        new_node = Node(value=val)
        for i in range(index):
            if current_node.next is None:
                raise IndexError("越界")
            pre_node = current_node
            current_node = current_node.next
        else:
            pre_node.next = new_node
            new_node.next = current_node

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        pre_node = None
        new_node = self._head
        for i in range(index):
            if new_node.next is None:
                raise IndexError("越界")
            pre_node = new_node
            new_node = new_node.next
        else:
            pre_node.next = new_node

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# # param_1 = obj.get(index)
# obj.addAtHead(1)
#
# obj.addAtTail(2)
# obj.addAtTail(3)
# obj.addAtIndex(1, 2333)
# param_0 = obj.get(0)
# param_1 = obj.get(1)
# param_2 = obj.get(2)
#
# print(param_0)
# print(param_1)
# print(param_2)

# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
