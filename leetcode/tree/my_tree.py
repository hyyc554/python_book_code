#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author    : Young
@Email     : hyc554@outlook.com
@site      : http://www.cnblogs.com/huang-yc/
@File      : my_tree.py
@version   : 1.0
@Time      : 2019/4/9 21:50
Description about this file:

"""


class Node(object):
    def __init__(self, value):
        """
        param: self.elem 是结点的数据域
                self.lchild 是结点的左孩子
                self.rchild 是结点的右孩子
        """
        self.val = value
        self.left = None
        self.right = None


class Tree(object):
    def __init__(self):
        self.root = None

    def add(self, item):
        """
        param: item 是传进来来的数据,我们要实例化一个结点取接收他,但是他的位置要放在树梢,不能乱插入
                queue 我们创建一个队列来接收和弹出结点,这样我们找到结点需要接收的位置
        """
        node = Node(item)
        if self.root is None:
            """如果根结点是None,是一颗空数,我们就把node赋值给root,那么下面的while循环是不会受影响的,因为是队列[None]的bool值是True"""
            self.root = node
            return
        queue = [self.root]
        while queue:
            """队列的弹出要加0,与栈相仿"""
            cur_node = queue.pop(0)
            if cur_node.left is None:
                """这里有空位,我们插入结点,如果能插入,就完事了"""
                cur_node.left = node
                return
            else:
                """cur_node的左孩子我们放进队列中,下次循环左子结点"""
                queue.append(cur_node.left)

            """同理对右边的操作一样,还是手敲下吧"""

            if cur_node.right is None:
                cur_node.right = node
                return
            else:
                queue.append(cur_node.right)
if __name__ == '__main__':

    my_tree = Tree()
    my_tree.add(1)
    my_tree.add(2)
