# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 00:23:42 2020

@author: AlvinChen
"""
import numpy as np
class Solution1:
    def productExceptSelf(self, nums):
        """
        input type:List[int]
        output type:List[int]
        """
        length=len(nums)
        if not length: return nums
        s=nums[0]
        for i in range(1,length):
            s*=nums[i]

        lst=np.array([s]*length)
        lst=lst/np.array(nums)
        return list(lst)

class Solution2:
    def productExceptSelf(self, nums):
        """
        input type:List[int]
        output type:List[int]
        """
        length=len(nums)
        if not length: return nums
        L,R=[1],[1]
        for i in range(1,length):
            L.append(L[i-1]*nums[i-1])
            R.append(R[i-1]*nums[length-i])
        lst=[L[i]*R[length-1-i] for i in range(length)]
        return lst

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [0]*length

        # answer[i] 表示索引 i 左侧所有元素的乘积
        # 因为索引为 '0' 的元素左侧没有元素， 所以 answer[0] = 1
        answer[0] = 1
        for i in range(1, length):
            answer[i] = nums[i - 1] * answer[i - 1]

        # R 为右侧所有元素的乘积
        # 刚开始右边没有元素，所以 R = 1
        R = 1;
        for i in reversed(range(length)):
            # 对于索引 i，左边的乘积为 answer[i]，右边的乘积为 R
            answer[i] = answer[i] * R
            # R 需要包含右边所有的乘积，所以计算下一个结果时需要将当前值乘到 R 上
            R *= nums[i]

        return answer

if __name__=="__main__":
    s=Solution()
#    steps=eval(input())
    print(s.productExceptSelf([1,2,3,4]))