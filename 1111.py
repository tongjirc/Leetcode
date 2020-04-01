# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 11:00:33 2020

@author: AlvinChen
"""
class Solution:
    def maxDepthAfterSplit(self, sequence):
        N=len(sequence)
        group=[]
        depth=[]
        for i,l in enumerate(sequence):
            if l=="(":
                d=len(depth)
                depth.append(d)
                group.append(d%2)
            if l==")":
                d=depth.pop()
                group.append(d%2)
        return group

if __name__=="__main__":
	s=Solution()
	sequence=input()
	print(s.maxDepthAfterSplit(sequence))
