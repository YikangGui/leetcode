def inOrder_Iterative(root, indexes):
    res = []
    stack = []
    node = 1
    while stack or node != -1:
        while node != -1:
            stack.append(node)
            node = indexes[node-1][0]
        node = stack.pop()
        res.append(node)
        node = indexes[node-1][1]
    return res

def inOrder_Recursive(root, indexes, ans):
    if root == -1:
        return
    inOrder_Recursive(indexes[root-1][0], indexes, ans)
    ans.append(root)
    inOrder_Recursive(indexes[root-1][1], indexes, ans)