# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 13:24:53 2020

@author: AlvinChen
"""
import numpy as np
class Solution:
    def numIslands(self, grid):
        """
        input type: list[list[str]]
        output type: int
        """
        numland=0
        if not grid or not grid[0]:
            return 0
        l1,l2=len(grid),len(grid[0])
        def dfs(x,y):
            grid[x][y]=numland
            for i,j in [[-1,0],[0,-1],[1,0],[0,1]]:
                x1,y1=x+i,y+j
                if 0<=x1<l1 and 0<=y1<l2 and grid[x1][y1]=="1":
                    dfs(x1,y1)
        for i,l in enumerate(grid):
            for j,m in enumerate(l):
                if grid[i][j]=="1":
                    numland-=1
                    dfs(i,j)
        return -numland


if __name__=="__main__":
    s=Solution()
    grid=eval(input())
    print(s.numIslands(grid))
