#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author    : Young
@Email     : hyc554@outlook.com
@site      : http://www.cnblogs.com/huang-yc/
@File      : cycle_link.py
@version   : 1.0
@Time      : 2019/4/7 19:36
Description about this file:

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        quick_pointer = slow_pointer = head             # 创建两个指针，分别记录一个快的遍历指针，和一个慢的便利指针

        while quick_pointer and quick_pointer.next:     # 当快指针为None，或快指针的下个一对象为None，说明不是环形链表
            slow_pointer = slow_pointer.next            # 慢指针前进一步
            quick_pointer = quick_pointer.next.next     # 快指针前进两步
            if slow_pointer == quick_pointer:           # 假如快指针等于慢指针，说明为环形链表
                return True
        return False


class Solution2(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        my_dict = {}                        # 创建一个字典来保存已经遍历过节点的内存地址
        while head and head.next:           # 当快指针为None，或快指针的下个一对象为None，说明不是环形链表
            if id(head) in my_dict:         # 假如当前节点在字典中则说明是环形链表
                return True
            else:
                my_dict[id(head)] = True    # 将当前节点加入到字典中

        return False


class Solution3(object):
    def reverse_list(self, head):
        before = after = None
        while head:
            after = head.next               # 保存当前节点的下一个节点
            head.next = before              # 将当前节点的下一题个节点替换为当前节点的上一个节点
            before = head                   # 将上一个节点，往前移动，变为当前节点
            head = after                    # 当前节点向前移动
        return before                       # 返回反转完成后的头结点

    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head and head.next and head == self.reverse_list(head):      # 加入反转后的头结点与原先的头结点相同，则说明有环
            return True
        return False
