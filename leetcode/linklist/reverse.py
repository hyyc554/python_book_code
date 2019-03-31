#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author    : Young
@Email     : hyc554@outlook.com
@site      : http://www.cnblogs.com/huang-yc/
@File      : reverse.py
@version   : 1.0
@Time      : 2019/3/24 11:35
Description about this file:

"""


# encoding: utf-8

class Node(object):
    def __init__(self):
        self.value = None
        self.next = None

    def __str__(self):
        return str(self.value)


def reverse_loop(head):
    """
    循坏迭代
    :param head:
    :return:
    """
    if not head or not head.next:
        return head
    pre = None
    while head:
        next = head.next  # 缓存当前节点的向后指针，待下次迭代用
        head.next = pre  # 这一步是反转的关键，相当于把当前的向前指针作为当前节点的向后指针
        pre = head  # 作为下次迭代时的（当前节点的）向前指针
        head = next  # 作为下次迭代时的（当前）节点
    return pre  # 返回头指针，头指针就是迭代到最后一次时的head变量（赋值给了pre）


def reverse_recursion(head):
    """
    递归法
    基准条件是将前置节点的下一位替换成自己，并将自己的下一个节点置空
    :param head:
    :return:
    """
    if not head or not head.next:                   # 处理边界情况
        return head

    new_head = reverse_recursion(head.next)

    head.next.next = head
    head.next = None
    return new_head


def link_list_producer(length):
    """
    用来生成一个python的链表对象，用以测试
    :param length: 链表的长度
    :return:
    """
    a = None
    b = None
    for i in range(length):
        b = a
        a = Node()
        a.value = i
        if i != 0:
            a.next = b

    return a


if __name__ == '__main__':

    # three = Node()
    # three.value = 3
    #
    # two = Node()
    # two.value = 2
    # two.next = three
    #
    # one = Node()
    # one.value = 1
    # one.next = two
    #
    # head = Node()
    # head.value = 0
    # head.next = one
    head = link_list_producer(4)

    newhead = reverse_recursion(head)
    while newhead:
        print(newhead.value, )
        newhead = newhead.next
