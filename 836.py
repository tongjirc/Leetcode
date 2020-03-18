# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 00:16:30 2020

@author: AlvinChen
"""
class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        return not (rec1[2] <= rec2[0] or
                    rec1[3] <= rec2[1] or
                    rec1[0] >= rec2[2] or
                    rec1[1] >= rec2[3])


if __name__=="__main__":
	s=Solution()
	rec1=eval(input())
	rec2=eval(input())
	print(s.isRectangleOverlap(rec1,rec2))
