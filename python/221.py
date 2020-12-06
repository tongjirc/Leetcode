# -*- coding: utf-8 -*-
"""
Created on Fri May  8 00:42:55 2020

@author: AlvinChen
"""

class Solution1:
    def maximalSquare(self, matrix):
        """
        input type:List[List[str]]
        output type:int
        """
        maxrec=0
        if not matrix or not matrix[0]:return maxrec
        l1,l2=len(matrix),len(matrix[0])

        def bfs(x,y):
            bfslst=[]
            now=1
            while True:
                now+=1
                bfslst=set([(x+now-1,j,now) for j in range(y,y+now)]+[(j,y+now-1,now) for j in range(x,x+now)])
                while bfslst:
                    x1,y1,n=bfslst.pop()
                    if x1>=l1 or y1>=l2 or matrix[x1][y1]!="1":return n-1

        for x in range(l1):
            for y in range(l2):
                if matrix[x][y]=="1":
                    num=bfs(x,y)
                    if maxrec<num:maxrec=num
        return maxrec**2

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        maxSide = 0
        rows, columns = len(matrix), len(matrix[0])
        dp = [[0] * columns for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    maxSide = max(maxSide, dp[i][j])

        maxSquare = maxSide * maxSide
        return maxSquare

if __name__=="__main__":
    try:
        a=Solution()
        n= eval(input())
        print(a.maximalSquare(n))
    except Exception as e:
        print(e)