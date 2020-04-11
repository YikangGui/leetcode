"""
Bellman-Ford是用来处理带有负值权重的有向图的最短路径的算法，它基于DP的思想，时间复杂度最差是O(N**3), N是vertice的数量。
可以拓展到无向图，类似dijkstra
"""


import collections
import math


def bellman_ford(graph, n, start):
    """
    :param graph: dict graph, value[0] is connected vertex, value[1] is the weight from [key, value[0]]
    :param n: no of vertice
    :param start: starting point
    :return: exist negative weight cycle, shortest distance from starting point
    """
    iter_num = n - 1
    dist = [math.inf] * n
    dist[start] = 0
    try:
        for _ in range(iter_num):
            change = False
            for key in graph:
                for node, weight in graph[key]:
                    if dist[node] > dist[key] + weight:
                        change = True
                        dist[node] = dist[key] + weight
            if not change:
                return False, dist
        change = False
        for key in graph:
            for node, weight in graph[key]:
                if dist[node] > dist[key] + weight:
                    change = True
                    dist[node] = dist[key] + weight
    except IndexError:
        return False, None
    if change:
        return True, None
    else:
        return False, dist

