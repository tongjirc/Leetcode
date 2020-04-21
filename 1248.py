# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 12:02:10 2020

@author: AlvinChen
"""
class Solution1:
    def numberOfSubarrays(self, nums,k):
        length=len(nums)
        if not length or k>length: return 0
        numcount=0
        for i in range(length):
            count=0
            for j in range(i,length):
                count+=nums[j]%2
                if count==k:
                    numcount+=1
                elif count>k:
                    break
                else:
                    pass
        return numcount

class Solution2:
    def numberOfSubarrays(self, nums,k):
        length=len(nums)
        if not length or k>length: return 0
        count,zcount=0,0
        maxl=[]
        for i in range(0,length):
            if nums[i]%2==0:zcount+=1
            else:
                if zcount!=0:
                    maxl.append(-zcount)
                    zcount=0
                count+=1
                maxl.append(count)
        else:
            if zcount!=0:maxl.append(-zcount)

        maxk,numbSub,lenmaxl=max(maxl),0,len(maxl)
        if maxk<k:return 0
        for i in range(1,maxk+1):
            if i+k-1>maxk:break
            left,right=maxl.index(i),maxl.index(i+k-1)
            if 0<=left-1 and maxl[left-1]<0:leftnum=1-maxl[left-1]
            else:leftnum=1
            if right+1<lenmaxl and maxl[right+1]<0:rightnum=1-maxl[right+1]
            else:rightnum=1
            numbSub+=rightnum*leftnum
        return numbSub

class Solution3:
    def numberOfSubarrays(self, nums,k):
        length=len(nums)
        if not length or k>length: return 0
        count,zcount=0,0
        maxl={}
        for i in range(0,length):
            if nums[i]%2==0:zcount+=1
            else:
                count+=1
                maxl.setdefault(count,[]).append(zcount)
                maxl.setdefault(count-1,[]).append(zcount)
                zcount=0
        else:
            maxl.setdefault(count,[]).append(zcount)
            del(maxl[0])
        maxk,numbSub=count,0
        if maxk<k:return 0
        for i in range(1,maxk+1):
            if i+k-1>maxk:break
            leftnum=1+maxl[i][0]
            rightnum=1+maxl[i+k-1][1]
            numbSub+=rightnum*leftnum
        return numbSub

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        odd = [-1]
        ans = 0
        for i in range(n):
            if nums[i] % 2 == 1:
                odd.append(i)
        odd.append(n)
        print(odd)
        for i in range(1, len(odd) - k):
            ans += (odd[i] - odd[i - 1]) * (odd[i + k] - odd[i + k - 1])
        return ans

if __name__=="__main__":
    try:
        a=Solution()
        nums,k= eval(input()),eval(input())
        print(a.numberOfSubarrays(nums,k))
    except Exception as e:
        print(e)