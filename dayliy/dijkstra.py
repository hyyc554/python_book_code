#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author    : Young
@Email     : hyc554@outlook.com
@site      : http://www.cnblogs.com/huang-yc/
@File      : dijkstra.py
@version   : 1.0
@Time      : 2019/1/16 22:51
Description about this file: 

"""

# 创建图
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}

print(graph)  # {'start': {'a': 6, 'b': 2}, 'a': {'fin': 1}, 'b': {'a': 3, 'fin': 5}, 'fin': {}}

# 创建开销表

infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity
print(infinity, type(infinity))

# 创建父节点
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None
# 用来记录处理过的节点
processed = []


def find_lower_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


node = find_lower_cost_node(costs)

while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lower_cost_node(costs)

print(costs)
