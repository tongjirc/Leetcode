# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 00:43:06 2020

@author: AlvinChen
"""
import numpy as np
class Solution1:
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        numset=set()
        relst=[]
        if len(intervals)==0:
            return []
        for i in intervals:
            numset=numset.union(set(np.arange(i[0],i[1]+0.5,0.5)))
        if len(numset)==0: return []
        numset=sorted(list(numset))
        minnum,N=numset[0],len(numset)
        for i in range(N):
            if i==N-1 or numset[i+1]!=numset[i]+0.5:
                relst.append([int(minnum),int(np.ceil(numset[i]))])
                if i!=N-1:minnum=numset[i+1]
            else:
                continue
        return relst



class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # 如果列表为空，或者当前区间与上一区间不重合，直接添加
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 否则的话，我们就可以与上一区间进行合并
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

if __name__=="__main__":
	s=Solution()
	intervals=eval(input())
	print(s.merge(intervals))