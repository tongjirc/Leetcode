# 给定一个大小为 n 的整数数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。 
# 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：[3,2,3]
# 输出：[3] 
# 
#  示例 2： 
# 
#  
# 输入：nums = [1]
# 输出：[1]
#  
# 
#  示例 3： 
# 
#  
# 输入：[1,1,1,3,3,2,2,2]
# 输出：[1,2] 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 5 * 10⁴ 
#  -10⁹ <= nums[i] <= 10⁹ 
#  
# 
#  
# 
#  进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1)的算法解决此问题。 
#  Related Topics 数组 哈希表 计数 排序 👍 449 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def majorityElement(self, nums):
        lst=collections.Counter(nums)
        length_min=len(nums)//3
        for item in list(lst.items()):
            if item[1]<=length_min:
                lst.pop(item[0])
        return list(lst.keys())

# leetcode submit region end(Prohibit modification and deletion)

so=Solution()
nums=[1,2,3,3,4]
print(so.majorityElement(nums))