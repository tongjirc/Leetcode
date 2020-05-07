# -*- coding: utf-8 -*-
"""
Created on Wed May  6 00:23:52 2020

@author: AlvinChen
"""
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dayset = set(days)
        durations = [1, 7, 30]

        @lru_cache(None)
        def dp(i):
            if i > 365:
                return 0
            elif i in dayset:
                return min(dp(i + d) + c for c, d in zip(costs, durations))
            else:
                return dp(i + 1)

        return dp(1)


if __name__=="__main__":
	s=Solution()
	x=eval(input())
	y=eval(input())
	z=eval(input())
	print(s.canMeasureWater(x,y,z))
