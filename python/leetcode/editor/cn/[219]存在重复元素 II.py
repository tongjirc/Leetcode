# 给你一个整数数组 nums 和一个整数 k ，判断数组中是否存在两个 不同的索引 i 和 j ，满足 nums[i] == nums[j] 且 abs(i 
# - j) <= k 。如果存在，返回 true ；否则，返回 false 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,3,1], k = 3
# 输出：true 
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,0,1,1], k = 1
# 输出：true 
# 
#  示例 3： 
# 
#  
# 输入：nums = [1,2,3,1,2,3], k = 2
# 输出：false 
# 
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  -10⁹ <= nums[i] <= 10⁹ 
#  0 <= k <= 10⁵ 
#  
#  Related Topics 数组 哈希表 滑动窗口 👍 376 👎 0


def Lst2ListNode(Lst):
    dummy = ListNode(-1, None)
    rcd = dummy
    for i in Lst:
        nd = ListNode(i, None)
        dummy.next = nd
        dummy = dummy.next
    return rcd.next


def ListNode2Lst(node):
    Lst = []
    while node:
        Lst.append(node.val)
        node = node.next
    return Lst


class ListNode(object):
    _name = "ListNode"

    def __init__(self, val=0, next=None, lst=[]):
        if not lst:
            self.val = val
            self.next = next
        else:
            self.val = lst.pop(0)
            if lst:
                self.next = ListNode(lst=lst)
            else:
                self.next = None

    def __str__(self):
        return str(ListNode2Lst(self))


class TreeNode:
    def __init__(self):
        self.id = None
        self.left = None
        self.right = None


from functools import reduce
from itertools import product


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dct_nums = {}
        for i in range(len(nums)):
            if dct_nums.get(nums[i]) is not None and i - dct_nums[nums[i]] <= k:
                return True
            dct_nums[nums[i]] = i
        return False


# leetcode submit region end(Prohibit modification and deletion)

so = Solution()
nums = [1,2,3,1,2,3]
k = 2
print(so.containsNearbyDuplicate(nums,k))
