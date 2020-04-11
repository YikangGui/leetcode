"""
Dijkstra algorithm 是用来解决 single source shortest path (单源最短路径)
Leetcode 743. Network Delay Time
Time complexity O(N**2), N is the num of vertices
原本是在有向图(directed graph)上操作，可以拓展到无向图(undirected graph)，因为在构建graph dict的时候，为每一个无向图的连接构造异向的两个connection即可
"""


import collections
import math


class Solution:
    def networkDelayTime(self, times, N: int, K: int) -> int:
        """
        :param times: 有向图的List表达. e.g [[2,1,1],[2,3,1],[3,4,1]]
        :param N: number of vertices
        :param K: starting point
        :return: max shortest path, if exist infinity, return -1
        """
        graph = collections.defaultdict(list)
        for time in times:
            graph[time[0] - 1].append(tuple([time[1] - 1, time[2]]))
        res = self.dijkstra(graph, K - 1, N)
        if res == math.inf:
            return -1
        else:
            return res

    def dijkstra(self, graph, start, n):
        """
        :param graph: dict graph, value[0] is connected vertex, value[1] is the weight from [key, value[0]]
        :param start: starting point
        :param n: number of vertices
        :return: shortest paths from starting point
        Time Complexity: O(n**2)
        """
        unvisited = set(list(range(n)))
        dist = [math.inf] * n
        dist[start] = 0
        cur_node = start

        while unvisited and not cur_node is None:
            unvisited.remove(cur_node)
            for node, weight in graph[cur_node]:
                # This step is called relaxation
                if node in unvisited and weight + dist[cur_node] < dist[node]:
                    dist[node] = weight + dist[cur_node]
            tmp_min = math.inf
            tmp_node = None
            for node in unvisited:
                if dist[node] < tmp_min:
                    tmp_node = node
                    tmp_min = dist[node]
            cur_node = tmp_node
        return max(dist)
