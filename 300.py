import collections

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp=[1 for i in nums]
        for i in range(0,len(nums)):
            for j in range(0,i):
                if nums[j]>nums[i]:
                    #j: previous stage i: current stage
                    dp[i]=max(dp[i],dp[j]+1)
        return max(dp)


if __name__=="__main__":
	s=Solution()
	nums=eval(input())
	print(s.lengthOfLIS(nums))