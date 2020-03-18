input = [[0, 1, 1, 0, 1],
 [0, 1, 0, 1, 0],
 [0, 0, 0, 0, 1],
 [0, 1, 0, 0, 0]]
input = [[0]]

def zombie(input):
    m = len(input)
    if m == 0: return 0
    n = len(input[0])
    if n == 0: return 0

    q = [(x,y,0) for x, i in enumerate(input) for y,j in enumerate(i) if j]

    if not q:
        return -1
    res = 0
    for x, y, level in q:
        res = max(res, level)
        for i, j in (x-1,y), (x+1,y), (x,y-1), (x,y+1):
            if 0 <= i < m and 0 <= j < n and input[i][j] == 0:
                input[i][j] = 1
                q.append((i,j,level+1))
    return res

print(zombie(input))