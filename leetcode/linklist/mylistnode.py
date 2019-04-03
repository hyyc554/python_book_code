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
        self.length = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if self._head is None:
            return -1
        new_node = self._head
        for i in range(self.length):
            if i == index:
                return new_node.val

            new_node = new_node.next


    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self._head = Node(value=val, next_=self._head)
        self.length += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        current_node = self._head
        while current_node.next is not None:
            current_node = current_node.next
        new_tail = Node(value=val, next_=None)
        current_node.next = new_tail
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        # 应对特殊情况
        # print(self.__length)
        if index == 0:
            self.addAtHead(val)
        elif index == self.length:
            print("wdasdasd")
            self.addAtTail(val)
        elif index > self.length:
            return -1
        else:
            node = Node(val)
            prior = self._head
            count = 1
            # 在插入位置的前一个节点停下
            while count < (self.length - 1):
                print("ok")
                prior = prior.next
                count += 1
            # 先将插入节点与节点后的节点连接，防止链表断掉，先链接后面的，再链接前面的
            node.next = prior.next
            prior.next = node
        self.length+=1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        pre_node = None
        current_node = self._head
        if index == 0:
            self._head = self._head.next
        elif index == self.length:
            current_node = self._head
            while current_node.next.next:
                current_node = current_node.next
            current_node.next = None

        elif index >= self.length:
            return -1
        else:

            for i in range(self.length):

                if i == index:
                    print(i)
                    # current_node.next = current_node.next.next.next

                    pre_node.next = current_node.next
                    self.length -= 1
                    return
                pre_node = current_node
                current_node = current_node.next


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
obj = MyLinkedList()

print(obj.addAtHead(1))
print(obj.addAtTail(3))
print(obj.addAtIndex(1, 2))

print(
    obj.length,obj.get(0),obj.get(1),obj.get(2))
print(obj.deleteAtIndex(1))
print(
    obj.length,obj.get(0),obj.get(1))
# print(obj.get(1))


# print(obj.get(1))
