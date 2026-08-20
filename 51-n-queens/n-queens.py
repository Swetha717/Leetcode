class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[["."]*n for _ in range(n)]
        res=[]
        def is_safe(row,col):
            for r in range (row-1,-1,-1):
                if board[r][col]=="Q":
                    return False
            r,c=row-1,col-1
            while r>=0 and c>=0:
                if board[r][c]=="Q":
                    return False
                r-=1
                c-=1
            r,c=row-1,col+1
            while c<n and r>=0:
                if board[r][c]=="Q":
                    return False
                r-=1
                c+=1
            return True
        def backtrack(row):
            if row==n:
                res.append(["".join(_) for _ in board])
                return
            for col in range(n):
                if is_safe(row,col):
                    board[row][col]="Q"
                    backtrack(row+1)
                    board[row][col]="."
        backtrack(0)
        return res