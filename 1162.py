# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 09:53:33 2020

@author: AlvinChen
"""
import numpy as np
class Solution:
    def maxDistance(self, island):
        npisland=np.array(island)
        npLst=np.inf*np.ones(npisland.shape)
        N=len(island)

        def bfs(x,y,n):
            for i,j in [(i1,j1) for i1 in range(-N+1,N) for j1 in range(-N+1,N) if abs(i1)+abs(j1)==n]:
                x1,y1=x+i,y+j
                if 0<=x1<N and 0<=y1<N:
                    if npisland[x1,y1]==1:
                        npLst[x1,y1]=0
                        return n
                else:
                    continue
            else:
                return bfs(x,y,n+1)

        if np.max(npisland)==0 or np.min(npisland)==1:
            return -1
        for i,j in [(i1,j1) for i1 in range(N) for j1 in range(N)]:
            if npLst[i,j]==np.inf:
                if npisland[i,j]==1:
                    npLst[i,j]=0
                elif npLst[i,j]==np.inf:
                    npLst[i,j]=bfs(i,j,0)
                else:
                    continue
        return int(np.max(npLst))

class Solution1:
    def maxDistance(self, grid: List[List[int]]) -> int:
        N = len(grid)

        queue = []
        # 将所有的陆地格子加入队列
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 1:
                    queue.append((i, j))
    	# 如果我们的地图上只有陆地或者海洋，请返回 -1。
        if len(queue) == 0 or len(queue) == N * N:
            return -1

        distance = -1
        while len(queue) > 0:
            distance += 1
            # 这里一口气取出 n 个结点，以实现层序遍历
            n = len(queue)
            for i in range(n):
                r, c = queue.pop(0)
                # 遍历上边单元格
                if r-1 >= 0 and grid[r-1][c] == 0:
                    grid[r-1][c] = 2
                    queue.append((r-1, c))
                # 遍历下边单元格
                if r+1 < N and grid[r+1][c] == 0:
                    grid[r+1][c] = 2
                    queue.append((r+1, c))
                # 遍历左边单元格
                if c-1 >= 0 and grid[r][c-1] == 0:
                    grid[r][c-1] = 2
                    queue.append((r, c-1))
                # 遍历右边单元格
                if c+1 < N and grid[r][c+1] == 0:
                    grid[r][c+1] = 2
                    queue.append((r, c+1))

        return distance

if __name__=="__main__":
	s=Solution()
	island=eval(input())
	print(s.maxDistance(island))
