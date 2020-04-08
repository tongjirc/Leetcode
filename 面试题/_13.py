# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 09:48:31 2020

@author: AlvinChen
"""

class Solution:
    def movingCount(self, m, n, k):
        if not m or not n:
            return 0
        board=[]
        def avilable(x,y):
            def sum_digit(n):
              sum=0
              a = n % 10
              n //= 10
              sum += a
              if n > 0 :
                 sum = sum + sum_digit(n)
              return sum
            if sum_digit(x)+sum_digit(y)>k:
                return False
            else:
                return True
        def dfs(x,y,count):
            if board[x][y]==0:
                count+=1
                board[x][y]=-1
                for i,j in [[-1,0],[0,-1],[1,0],[0,1]]:
                    x1,y1=x+i,y+j
                    if 0<=x1<m and 0<=y1<n and board[x1][y1]!=-1:
                        count=dfs(x1,y1,count)
            return count

        for i in range(m):
            row=[]
            for j in range(n):
                if avilable(i,j):row.append(0)
                else:row.append(1)
            board.append(row)
        return dfs(0,0,0)



if __name__=="__main__":
    try:
        s=Solution()
        m,n,k=eval(input()),eval(input()),eval(input())
        print(s.movingCount(m,n,k))
    except Exception as e:
        print(e)