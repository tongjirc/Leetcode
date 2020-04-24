# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 10:23:44 2020

@author: AlvinChen
"""
import time
class Solution1:
    def reversePairs(self, nums):
        """
        input type: List[int]
        output type: int
        """
        if not nums:return 0
        length=len(nums)
        numpairs=0
        for i in range(0,length):
            for j in range(i, length):
                if nums[i]>nums[j]:
                    numpairs+=1
        return numpairs

class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = [0]
        def Merge_sort(s):
            n = len(s)
            if n < 2:
                return
            mid = n // 2
            s1 = s[0:mid]
            s2 = s[mid:n]
            Merge_sort(s1)
            Merge_sort(s2)
            Merge(s1,s2,s)

        def Merge(s1,s2,s):
            len_s1 = len(s1) - 1
            len_s2 = len(s2) - 1
            temp = len(s) - 1

            while len_s1 >=0 and len_s2 >= 0:
                if s1[len_s1] > s2[len_s2]:
                    s[temp] = s1[len_s1]
                    result[0] += len_s2 + 1
                    len_s1 -= 1
                    temp -= 1
                else:
                    s[temp] = s2[len_s2]
                    len_s2 -= 1
                    temp -= 1

            while len_s1 >= 0:
                s[temp] = s1[len_s1]
                len_s1 -= 1
                temp -= 1
            while len_s2 >= 0:
                s[temp] = s2[len_s2]
                temp -= 1
                len_s2 -= 1

        Merge_sort(nums)
        return result[0]


if __name__=="__main__":
    nums=eval(input())
    start=time.time()
    s=Solution1()
    print(s.reversePairs(n))
    print(time.time()-start)
    start=time.time()
    s=Solution()
    print(s.reversePairs(n))
    print(time.time()-start)