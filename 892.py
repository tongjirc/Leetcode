# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 22:29:48 2020

@author: AlvinChen
"""
import collections

class Solution:
    def surfaceArea(self, grid):
        res_area = 0
        hide_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    res_area += grid[i][j]
                    hide_area += grid[i][j] - 1
                if i > 0:
                    hide_area += min(grid[i-1][j], grid[i][j])
                if j > 0:
                    hide_area += min(grid[i][j-1], grid[i][j])
        return res_area*6 - hide_area*2


if __name__=="__main__":
	s=Solution()
	words=eval(input())
	print(s.surfaceArea(words))
