# 给你一个按递增顺序排序的数组 arr 和一个整数 k 。数组 arr 由 1 和若干 素数 组成，且其中所有整数互不相同。 
# 
#  对于每对满足 0 < i < j < arr.length 的 i 和 j ，可以得到分数 arr[i] / arr[j] 。 
# 
#  那么第 k 个最小的分数是多少呢? 以长度为 2 的整数数组返回你的答案, 这里 answer[0] == arr[i] 且 answer[1] == 
# arr[j] 。 
#  
# 
#  示例 1： 
# 
#  
# 输入：arr = [1,2,3,5], k = 3
# 输出：[2,5]
# 解释：已构造好的分数,排序后如下所示: 
# 1/5, 1/3, 2/5, 1/2, 3/5, 2/3
# 很明显第三个最小的分数是 2/5
#  
# 
#  示例 2： 
# 
#  
# 输入：arr = [1,7], k = 1
# 输出：[1,7]
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= arr.length <= 1000 
#  1 <= arr[i] <= 3 * 10⁴ 
#  arr[0] == 1 
#  arr[i] 是一个 素数 ，i > 0 
#  arr 中的所有数字 互不相同 ，且按 严格递增 排序 
#  1 <= k <= arr.length * (arr.length - 1) / 2 
#  
#  Related Topics 数组 二分查找 堆（优先队列） 👍 153 👎 0
import itertools
from functools import reduce
from itertools import product


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def kthSmallestPrimeFraction(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        ls_prime = []
        for i in range(len(arr)-1):
            for j in range(i+1,len(arr)):
                ls_prime.append([arr[i],arr[j]])
        length = len(ls_prime)

        def partition(left, right):
            key = left
            while left < right:
                while left < right and ls_prime[key][0] / ls_prime[key][1] <= ls_prime[right][0] / ls_prime[right][1]:
                    right -= 1
                while left < right and ls_prime[left][0] / ls_prime[left][1] <= ls_prime[key][0] / ls_prime[key][1]:
                    left += 1
                ls_prime[left], ls_prime[right] = ls_prime[right], ls_prime[left]
            ls_prime[key], ls_prime[right] = ls_prime[right], ls_prime[key]
            return right

        def fast_sort(left, right):
            if left >= right:
                return left
            mid = partition(left, right)
            if mid > k-1:
                return fast_sort(left, mid - 1)
            elif mid < k-1:
                return fast_sort(mid + 1, right)
            else:
                return mid

        return ls_prime[fast_sort(0, length - 1)]


# leetcode submit region end(Prohibit modification and deletion)

so = Solution()
arr, k = [1, 2, 3, 5], 3
print(so.kthSmallestPrimeFraction(arr, k))
