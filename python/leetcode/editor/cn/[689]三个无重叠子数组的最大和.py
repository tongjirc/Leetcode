# 给你一个整数数组 nums 和一个整数 k ，找出三个长度为 k 、互不重叠、且 3 * k 项的和最大的子数组，并返回这三个子数组。 
# 
#  以下标的数组形式返回结果，数组中的每一项分别指示每个子数组的起始位置（下标从 0 开始）。如果有多个结果，返回字典序最小的一个。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,1,2,6,7,5,1], k = 2
# 输出：[0,3,5]
# 解释：子数组 [1, 2], [2, 6], [7, 5] 对应的起始下标为 [0, 3, 5]。
# 也可以取 [2, 1], 但是结果 [1, 3, 5] 在字典序上更大。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,1,2,1,2,1,2,1], k = 2
# 输出：[0,2,4]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 2 * 10⁴ 
#  1 <= nums[i] < 2¹⁶ 
#  1 <= k <= floor(nums.length / 3) 
#  
#  Related Topics 数组 动态规划 👍 220 👎 0


from functools import reduce
from itertools import product


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        f3 = [[float("-inf"), [i] * 3] for i in range(-k - 1, 0)]
        f2 = [[float("-inf"), [i] * 2] for i in range(-k - 1, 0)]
        f1 = [[float("-inf"), [i] * 1] for i in range(-k - 1, 0)]
        for i in range(len(nums) - k + 1):
            f1.pop(0)
            f2.pop(0)
            f3.pop(0)
            # f1
            tmp = sum(nums[i:i + k])
            if tmp > f1[-1][0]:
                f1.append([tmp, [i]])
            else:
                f1.append(f1[-1])
            # f2
            if tmp + f1[0][0] > f2[-1][0]:
                f2.append([tmp + f1[0][0], f1[0][1] + [i]])
            else:
                f2.append(f2[-1])
            # f3
            if tmp + f2[0][0] > f3[-1][0]:
                f3.append([tmp + f2[0][0], f2[0][1] + [i]])
            else:
                f3.append(f3[-1])
        return f3[-1][1]


# leetcode submit region end(Prohibit modification and deletion)

so = Solution()
nums = [1, 2, 1, 2, 6, 7, 5, 1]
k = 2
print(so.maxSumOfThreeSubarrays(nums, k))
