import collections

class Solution1(object):
    def majorityElement(self, nums):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        maj=None
        dict={}
        N=len(nums)
        for i in range(0,N):
        	k=str(nums.pop())
        	if k in dict.keys():
        		dict[k]+=1
        	else:
        		dict[k]=1
        	if dict[k] > int(N/2):
        		maj= int(k)
        		break
        return maj

class Solution:
	"""
	:Hash list
	"""
	def majorityElement(self, nums):
		counts = collections.Counter(nums)
		return max(counts.keys(), key=counts.get)

if __name__=="__main__":
	s=Solution()
	nums=eval(input())
	print(s.majorityElement(nums))