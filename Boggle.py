dictionary = ["GEEKSG", "FOR", "QUIZZ", "GO"]
boggle = [['G','I','Z'],
          ['U','E','K'],
          ['Q','S','E']]


def boggleWords(dictionary=dictionary, boggle=boggle):
    m = len(boggle)
    if m == 0: return None

    n = len(boggle[0])
    if n == 0: return None

    res = set()

    def dfs(i, j, strs, pointer):
        if pointer == len(strs):
            res.add(strs)
            return
        if 0 <= i < m and 0 <= j < n:
            if boggle[i][j] == strs[pointer]:
                dfs(i-1, j-1, strs, pointer+1)
                dfs(i-1, j, strs, pointer+1)
                dfs(i-1, j+1, strs, pointer+1)
                dfs(i, j+1, strs, pointer+1)
                dfs(i+1, j+1, strs, pointer+1)
                dfs(i+1, j, strs, pointer+1)
                dfs(i+1, j-1, strs, pointer+1)
                dfs(i, j-1, strs, pointer+1)

    for word in dictionary:
        for i in range(m):
            if word in res: break
            for j in range(n):
                if word in res: break
                dfs(i, j, word, 0)
    if res:
        return res
    else:
        return -1


print(boggleWords())
