#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author    : Young
@Email     : hyc554@outlook.com
@site      : http://www.cnblogs.com/huang-yc/
@File      : mycircularqueue.py
@version   : 1.0
@Time      : 2019/4/11 20:06
Description about this file:

"""


class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.queue = [None] * (k + 1)
        self.maxsize = k + 1
        self.front = 0
        self.tail = 0

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.maxsize
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.maxsize
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """

        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.queue[self.tail-1]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.front == self.tail

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return (self.tail + 1) % self.maxsize == self.front


if __name__ == '__main__':
    a =MyCircularQueue(3)
    print(a.enQueue(1))
    print(a.enQueue(2))
    print(a.enQueue(3))
    print(a.enQueue(4))
    print(a.Rear())
    print(a.isFull())
    print(a.deQueue())
    print(a.enQueue(4))
    print(a.Rear())
    print(a.queue)
    print(a.Front())

