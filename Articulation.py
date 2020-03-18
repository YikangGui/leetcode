class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        linkedNodes = [[] for _ in range(n)]
        for connection in connections:
            linkedNodes[connection[0]].append(connection[1])
            linkedNodes[connection[1]].append(connection[0])
        exploreNodes = [True for _ in range(n)]

        dfn = [-1] * n
        low = [-1] * n

        res_edge = []
        res_vertex = set()
        dfn[0] = 0
        low[0] = 0
        exploreNodes[0] = False
        level = 1
        root = 0
        root_child = [0]

        def dfs(currentNode, prevNode, level):
            for node in linkedNodes[currentNode]:
                if exploreNodes[node]:
                    exploreNodes[node] = False
                    dfn[node] = level
                    low[node] = level
                    level = level + 1
                    dfs(node, currentNode, level)
                    low[currentNode] = min(low[currentNode], low[node])
                    if low[node] > dfn[currentNode]:
                        res_edge.append([currentNode, node])
                    if low[node] >= dfn[currentNode] and currentNode != 0:
                        res_vertex.add(currentNode)
                    if currentNode == 0:
                        root_child[0] += 1
                elif node == prevNode:
                    continue
                else:
                    low[currentNode] = min(dfn[node], low[currentNode])

        dfs(0, -1, level)
        if root_child[0] > 1:
            res_vertex.add(root)
        print(list(res_vertex))
        return res_edge
