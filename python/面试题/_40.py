# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 17:01:21 2020

@author: AlvinChen
"""
class Solution:
    def getLeastNumbers(self, arr,k):
        output=[]
        arr.sort()
        for i in range(k):
            output.append(arr[i])
        return ouput


if __name__=="__main__":
	s=Solution()
	arr=eval(input())
	k=eval(input())
	print(s.getLeastNumbers(arr,k))
