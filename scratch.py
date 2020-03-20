# Maximum Student Taking Exams

class Solution:
    def maxStudents(self, seats) -> int:
        m = len(seats)
        n = len(seats[0])
        bin_seats = []
        for row in seats:
            tmp_row = ''
            for seat in row:
                tmp_seat = 1 if seat == '.' else 0
                tmp_row += str(tmp_seat)
            bin_seats.append(int(tmp_row, 2))

        dp = [[0] * 2 ** n for _ in range(2)]
        v = bin_seats[0]
        x = v
        while x:
            if (x >> 1) & x == 0:
                dp[0][x] = bin(x).count('1')
            x = (x - 1) & v

        for i in range(1, m):
            v_last = bin_seats[i - 1]
            x = v_last

            while True:
                v_cur = bin_seats[i]
                y = v_cur
                while True:
                    if (y >> 1) & y == 0 and (x >> 1) & y == 0 and (y >> 1) & x == 0:
                        dp[1][y] = max(dp[1][y], dp[0][x] + bin(y).count('1'))
                    if y == 0:
                        break
                    y = (y - 1) & v_cur
                if x == 0:
                    break
                x = (x - 1) & v_last
            dp[0] = dp[1]
            dp[1] = [0] * 2 ** n
        return max(dp[0])


seats = [["#",".","#","#",".","#"],[".","#","#","#","#","."],["#",".","#","#",".","#"]]
seats = [["#",".","."],[".","#","."]]
seats = [[".",".","#","#"],[".","#",".","."],["#",".",".","#"],["#","#","#","."]]
seats = [["#",".","#","#",".","#"],[".","#","#","#","#","."],["#",".","#","#",".","#"]]
seats = [['#','.','.','.','#'],['.','#','.','#','.'],['.','.','#','.','.'],['.','#','.','#','.'],['#','.','.','.','#']]
solution = Solution()
print(solution.maxStudents(seats))