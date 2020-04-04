# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 21:50:27 2020

@author: AlvinChen
"""
class Solution1:
    def trap(self, height):
        if not height:
            return 0
        MaxH=max(height)
        everyrow=[]
        num=0
        for i in range(1,MaxH+1):
            row=""
            for j in range(len(height)):
                if height[j]>=i:
                    row+="1"
                else:
                    row+="0"
            everyrow.append(row)
        for lst in everyrow:
            left=lst.find("1")
            right=lst.rfind("1")
            if left==right:
                break
            else:
                for k in lst[left+1:right]:
                    if k=="0":
                        num+=1
        return num

import collections
class Solution:
    def trap(self, height):
        if not height:
            return 0
        arrayH=height.sort()
        everyrow=[]
        num=0
        for i in range(1,MaxH+1):
            row=""
            for j in range(len(height)):
                if height[j]>=i:
                    row+="1"
                else:
                    row+="0"
            everyrow.append(row)
        for lst in everyrow:
            left=lst.find("1")
            right=lst.rfind("1")
            if left==right:
                break
            else:
                for k in lst[left+1:right]:
                    if k=="0":
                        num+=1
        return num

if __name__=="__main__":
    try:
        a=Solution()
        height= eval(input())
        print(a.trap(height))
    except Exception as e:
        print(e)