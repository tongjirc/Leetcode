# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 17:01:21 2020

@author: AlvinChen
"""
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x + y < z:
            return False
        if x == 0 or y == 0:
            return z == 0 or x + y == z
        return z % math.gcd(x, y) == 0


if __name__=="__main__":
	s=Solution()
	x=eval(input())
	y=eval(input())
	z=eval(input())
	print(s.canMeasureWater(x,y,z))
