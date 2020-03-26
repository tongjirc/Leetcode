# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 19:23:51 2020

@author: AlvinChen
"""
import numpy as np
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        lst=[1,1,1,1]
        board=np.array(board)
        rx,ry=np.where(board=='R')
        def bfs(n):
            k=0
            for i in range(0,4):
                if i==0:
                    x,y=rx,ry-lst[i]
                elif i==1:
                    x,y=rx+lst[i],ry
                elif i==2:
                    x,y=rx,ry+lst[i]
                else:
                    x,y=rx-lst[i],ry
                if x < 0 or  y < 0 or x>7 or  y>7:
                    lst[i]=10
                    k+=1
                elif board[x,y]=='p':
                    n+=1
                    lst[i]+=1
                    lst[i]=10
                elif board[x,y]=='B':
                    lst[i]=10
                else:
                    lst[i]+=1
            if k==4:
                return n
            else:
                return bfs(n)
        nums = bfs(0)
        return nums

if __name__=="__main__":
	s=Solution()
	words=eval(input())
	print(s.middleNode(words))
