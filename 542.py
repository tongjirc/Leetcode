# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 12:20:31 2020

@author: AlvinChen
"""
class Solution:

    def updateMatrix(self, matrix):
        dis=matrix
        for i,m in enumerate(matrix):
            for j,l in enumerate(m):
                dis[i][j]=self.bfs(matrix=matrix,ans=0,lisloc=[[i,j]])
        return dis

    def bfs(self,matrix,ans,lisloc):
        newlst=[]
        for i,j in lisloc:
            if i<0 or j<0 or i>len(matrix)-1 or j >len(matrix[i])-1:
                continue
            if matrix[i][j]==0:
                return ans
            else:
                for x,y in [[1,0],[0,1],[-1,0],[0,-1]]:
                    newlst.append([i+x,j+y])
        return self.bfs(matrix,ans+1,newlst) if len(newlst)!=0 else 100000


if __name__=="__main__":
	s=Solution()
	nums=eval(input())
	print(s.updateMatrix(nums))
