# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 00:05:27 2020

@author: AlvinChen
"""
class Solution(object):
    def gameOfLife(self, boards):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        neighbors=[(i1,j1) for i1 in [1,0,-1] for j1 in [1,0,-1]]
        m=len(boards)
        if m>=1:
            n=len(boards[0])
        if m==0 or n==0:
            return boards
        nextboard=[]
        for i,l in enumerate(boards):
            nextboard.append(l.copy())

        for i,l in enumerate(nextboard):
            for j,k in enumerate(l):
                if nextboard[i][j]==0:
                    live=0
                    for i2,j2 in neighbors:
                        if i2==j2==0:
                            continue
                        x=i+i2
                        y=j+j2
                        if 0<=x<m and 0<=y<n and nextboard[x][y]==1:
                            live+=1
                    if live==3:
                        boards[i][j]=1

                if nextboard[i][j]==1:
                    live=0
                    for i2,j2 in neighbors:
                        if i2==j2==0:
                            continue
                        x=i+i2
                        y=j+j2
                        if 0<=x<m and 0<=y<n and nextboard[x][y]==1:
                            live+=1
                            if live>3:
                                boards[i][j]=0
                                break
                    if live<2:
                        boards[i][j]=0
                    if live==2 or live==3:
                        boards[i][j]=1

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        原地更新
        """

        neighbors = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]

        rows = len(board)
        cols = len(board[0])

        # 遍历面板每一个格子里的细胞
        for row in range(rows):
            for col in range(cols):

                # 对于每一个细胞统计其八个相邻位置里的活细胞数量
                live_neighbors = 0
                for neighbor in neighbors:

                    # 相邻位置的坐标
                    r = (row + neighbor[0])
                    c = (col + neighbor[1])

                    # 查看相邻的细胞是否是活细胞
                    if (r < rows and r >= 0) and (c < cols and c >= 0) and abs(board[r][c]) == 1:
                        live_neighbors += 1

                # 规则 1 或规则 3
                if board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    # -1 代表这个细胞过去是活的现在死了
                    board[row][col] = -1
                # 规则 4
                if board[row][col] == 0 and live_neighbors == 3:
                    # 2 代表这个细胞过去是死的现在活了
                    board[row][col] = 2

        # 遍历 board 得到一次更新后的状态
        for row in range(rows):
            for col in range(cols):
                if board[row][col] > 0:
                    board[row][col] = 1
                else:
                    board[row][col] = 0

if __name__=="__main__":
	s=Solution()
	boards=eval(input())
	print(s.gameOfLife(boards))