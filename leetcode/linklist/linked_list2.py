#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author    : Young
@Email     : hyc554@outlook.com
@site      : http://www.cnblogs.com/huang-yc/
@File      : linked_list2.py
@version   : 1.0
@Time      : 2019/4/5 11:06
Description about this file:

"""


class Node():
    """
    单链表中的节点应该具有两个属性：val 和 next。
    val 是当前节点的值，
    next 是指向下一个节点的指针/引用。
    """

    def __init__(self, value):
        # 存放元素数据
        self.val = value
        # next是下一个节点的标识
        self.next = None


class SingleLinkList():
    def __init__(self, node=None):
        # 头节点定义为私有变量
        self._head = node

    def is_empty(self):
        # 判断链表是否为空
        if self._head is None:
            return True
        else:
            return False

    def get(self, index: int) -> int:
        """
        获取链表中第 index 个节点的值。如果索引无效，则返回-1
        :param index: 索引值
        :return:
        """
        if self._head is None:
            return -1
        cur = self._head
        for i in range(index):
            if cur.next is None:
                return -1
            cur = cur.next
        return cur.val

    def length(self):
        """
        cur游标，用来移动遍历节点
        count用来计数
        :return: 返回链表的长度
        """
        cur = self._head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """
        遍历整个链表
        :return:
        """
        cur = self._head
        while cur is not None:
            print(cur.elem, end=' ')
            cur = cur.next

    def add_at_head(self, val: int) -> None:
        """
        在头部添加一个节点
        :param val:
        :return: None
        """
        # 先创建一个保存item值的节点
        node = Node(val)
        # 判断链表是否为空
        if self._head is None:
            self._head = node
        else:
            # 将新节点的链接域next指向头节点，即_head指向的位置
            node.next = self._head
            # 将链表的头_head指向新节点
            self._head = node

    def add_at_tail(self, val: int) -> None or int:
        """
        在尾部添加一个节点
        :param item:
        :return:
        """
        node = Node(val)
        # 若链表为空，直接将该节点作为链表的第一个元素
        if self._head is None:
            self._head = node
        else:
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def add_at_index(self, index: int, val: int) -> None:
        """
        在指定位置pos添加节点
        pos从0开始
        :param index:
        :param val:
        :return:
        """
        # 若指定位置pos为第一个元素之前，则执行头部插入
        if index <= 0:
            self.add_at_head(val)
        # 若指定位置超过链表尾部，则执行尾部插入
        elif index >= self.length():
            self.add_at_tail(val)
        # 找到指定位置
        else:
            # pre用来指向指定位置pos的前一个位置pos-1，初始从头节点开始移动到指定位置
            pre = self._head
            count = 0
            node = Node(val)
            # 在目标节点的前一位停下
            while count < (index - 1):
                count += 1
                pre = pre.next
            # 先将新节点node的next指向插入位置的节点
            node.next = pre.next
            # 将插入位置的前一个节点的next指向新节点
            pre.next = node

    def delete_at_index(self, index: int) -> None or int:
        """
        如果索引 index 有效，则删除链表中的第 index 个节点。
        :param index: 对应的索引值
        :return: -1表示为异常
        """
        pre = None
        cur = self._head
        if index is 0:
            self._head = None
        for i in range(index):
            if cur.next is None:
                # raise IndexError("越界")
                return -1
            pre = cur
            cur = pre.next
        else:
            pre.next = cur.next

    def search(self, val: int) -> True or False:
        """
        查找节点是否存在
        :param val: 节点的val值
        :return:
        """
        cur = self._head
        while cur is not None:
            if cur.val == val:
                return True
            else:
                cur = cur.next
        return False


if __name__ == '__main__':
    obj = SingleLinkList()
    obj.add_at_head(1)
    obj.add_at_tail(3)
    obj.add_at_index(1, 2)
    obj.travel()
    obj.delete_at_index(1)
    obj.travel()
