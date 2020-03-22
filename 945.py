# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 11:02:43 2020

@author: AlvinChen
"""
class Solution:
#    def minIncrementForUnique(self, words):
#        nums=0
#        words.sort()
#        i=1
#        while i <len(words):
#            if words[i]==words[i-1]:
#                words[i]+=1
#                j=i+1
#                while j<len(words) and words[j]<words[j-1]:
#                    t=words[j]
#                    words[j]=words[j-1]
#                    words[j-1]=t
#                    j+=1
#                nums+=1
#            else:
#                i+=1
#        return nums
    def minIncrementForUnique(self, A):
        A.sort()
        res = 0
        for i in range(1,len(A)):
            if A[i] <= A[i-1]:
                res += A[i-1]-A[i]+1
                A[i] = A[i-1]+1
        return res

def f(x,i=0):
    if(i==0):
        return((x-4.709)*(x-2.194)*(x-0.097))
    if(i==1):
        return([x/((4.709-2.194)*(4.709-0.097)),x/((2.194-4.709)*(2.194-0.097)),x/((0.097-4.709)*(0.097-2.194))])

if __name__=="__main__":
	s=Solution()
	words=eval(input())
	print(s.minIncrementForUnique(words))
