# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 00:16:30 2020

@author: AlvinChen
"""
class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        def intersect(p_left, p_right, q_left, q_right):
            return min(p_right, q_right) > max(p_left, q_left)
        return (intersect(rec1[0], rec1[2], rec2[0], rec2[2]) and
                intersect(rec1[1], rec1[3], rec2[1], rec2[3]))



if __name__=="__main__":
	s=Solution()
	rec1=eval(input())
	rec2=eval(input())
	print(s.isRectangleOverlap(rec1,rec2))
