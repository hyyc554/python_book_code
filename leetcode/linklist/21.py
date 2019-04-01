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
        self.val = None
        self.next = None

    def __str__(self):
        return str(self.val)


def mergeTwoLists(l1, l2):
    # 处理边界情况（l1或l2为空）
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    # 确保l1有最小的初始值
    if l2.val < l1.val:
        l1, l2 = l2, l1
    # 保存一个链表头用来作为返回值
    head = l1
    # 开始迭代到l1为最后一个节点
    while l1.next is not None:
        # 假如l2完结，工作完成
        if l2 is None:
            return head
        # 假如l2节点属于在l1的当前节点与下一个节点值之间
        if l1.val <= l2.val <= l1.next.val:
            # 在这一步我们通过设置l1.next\l2.next来拼接l2，并将L2 迭代
            l1.next, l2.next, l2 = l2, l1.next, l2.next
        # l1迭代向前
        l1 = l1.next
    # 以防l2较长的情况，我们在l1迭代完成后把l2加入到l1尾部
    l1.next = l2
    return head


if __name__ == '__main__':

    three = Node()
    three.val = 3

    two = Node()
    two.val = 2
    two.next = three

    one = Node()
    one.val = 1
    one.next = two

    head = Node()
    head.val = 0
    head.next = one

    three1 = Node()
    three1.val = 3

    two1 = Node()
    two1.val = 2
    two1.next = three1

    one1 = Node()
    one1.val = 1
    one1.next = two1

    head1 = Node()
    head1.val = 0
    head1.next = one1
    newhead = mergeTwoLists(head, head1)
    while newhead:
        print(newhead.val, )
        newhead = newhead.next
