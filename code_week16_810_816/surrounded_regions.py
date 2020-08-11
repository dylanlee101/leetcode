'''
给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。

找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

示例:

X X X X
X O O X
X X O X
X O X X
运行你的函数后，矩阵变为：

X X X X
X X X X
X X X X
X O X X

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/surrounded-regions
'''
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        n,m = len(board),len(board[0])
        que = collections.deque()
        for i in range(n):
            if board[i][0] == 'O':
                que.append((i,0))
            if board[i][m-1] == 'O':
                que.append((i,m-1))
        for i in range(m-1):
            if board[0][i] == 'O':
                que.append((0,i))
            if board[n-1][i] == 'O':
                que.append((n-1,i))
        while que:
            x,y = que.popleft()
            board[x][y] = 'A'
            for mx,my in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                if 0<= mx < n and 0 <= my < m and board[mx][my] == 'O':
                    que.append((mx,my))
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'A':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'