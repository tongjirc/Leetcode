# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 08:51:44 2020

@author: AlvinChen
"""

class Solution1:
    def spiralOrder(self, matrix):
        """
        false
        input type: List[List[int]]
        output type:List[int]
        """
        lst=[]
        if not matrix or not matrix[0]:return lst
        l1,l2=len(matrix),len(matrix[0])
        x,y=0,0
        while True:
            lst.append(matrix[x][y])
            matrix[x][y]=None
            for x1,y1 in [[x,y+1],[x-1,y],[x,y-1],[x+1,y]]:
                if 0<=x1<l1 and 0<=y1<l2 and matrix[x1][y1]!=None:
                    x,y=x1,y1
                    break
            else:
                break
        return lst

import copy
class Solution:
    def spiralOrder(self, matrix):
        """
        input type: List[List[int]]
        output type:List[int]
        """
        lst=[]
        orderlst=[[0,1],[-1,0],[0,-1],[1,0]]
        nextorderlst=[[0,1],[-1,0],[0,-1],[1,0]]
        diff=False
        if not matrix or not matrix[0]:return lst
        l1,l2=len(matrix),len(matrix[0])
        x,y=0,0
        while True:
            if diff:
                diff=False
                orderlst=copy.copy(nextorderlst)
            lst.append(matrix[x][y])
            matrix[x][y]=None
            for i,j in orderlst:
                x1,y1=x+i,y+j
                if 0<=x1<l1 and 0<=y1<l2 and matrix[x1][y1]!=None:
                    x,y=x1,y1
                    break
                else:
                    diff=True
                    nextorderlst.append(nextorderlst.pop(0))
            else:
                break
        return lst

if __name__=="__main__":
    try:
        a=Solution()
        matrix= eval(input())
        print(a.spiralOrder(matrix))
    except Exception as e:
        print(e)