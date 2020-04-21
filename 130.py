# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 00:12:40 2020

@author: AlvinChen
"""
class Solution:
    def solve(self, board):
        if not board or not board[0]:
            return board
        l1,l2=len(board),len(board[0])

        def dfs(x,y):
            board[x][y]="K"
            for i,j in [[-1,0],[0,-1],[1,0],[0,1]]:
                x1,y1=x+i,y+j
                if 0<=x1<l1 and 0<=y1<l2 and board[x1][y1]=="O":
                    dfs(x1,y1)
        def bfs(bfslst):
            while bfslst:
                x,y=bfslst.pop(0)
                board[x][y]="K"
                for i,j in [[-1,0],[0,-1],[1,0],[0,1]]:
                    x1,y1=x+i,y+j
                    if 0<=x1<l1 and 0<=y1<l2 and board[x1][y1]=="O" and (x1,y1) not in bfslst:
                        bfslst.append((x1,y1))
        ls1=[(i1,j1) for i1 in [0,l1-1] for j1 in range(l2)]
        ls1.extend([(i2,j2) for i2 in range(l1) for j2 in [0,l2-1]])
        for i,j in ls1:
            if board[i][j]=="O":
                bfs([(i,j)])
#                dfs(i,j)
        for i in range(l1):
            for j in range(l2):
                if board[i][j]=="O":
                    board[i][j]="X"
                if board[i][j]=="K":
                    board[i][j]="O"
        return board



if __name__=="__main__":
    try:
        a=Solution()
        board= eval(input())
        print(a.solve(board))
    except Exception as e:
        print(e)