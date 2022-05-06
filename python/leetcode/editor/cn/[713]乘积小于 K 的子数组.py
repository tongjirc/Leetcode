# 给你一个整数数组 nums 和一个整数 k ，请你返回子数组内所有元素的乘积严格小于 k 的连续子数组的数目。
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [10,5,2,6], k = 100
# 输出：8
# 解释：8 个乘积小于 100 的子数组分别为：[10]、[5]、[2],、[6]、[10,5]、[5,2]、[2,6]、[5,2,6]。
# 需要注意的是 [10,5,2] 并不是乘积小于 100 的子数组。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,3], k = 0
# 输出：0 
# 
#  
# 
#  提示: 
# 
#  
#  1 <= nums.length <= 3 * 10⁴ 
#  1 <= nums[i] <= 1000 
#  0 <= k <= 10⁶ 
#  
#  Related Topics 数组 滑动窗口 👍 475 👎 0


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
        self.val = None
        self.left = None
        self.right = None


import time
from functools import reduce
from itertools import product
from memory_profiler import profile


# leetcode submit region begin(Prohibit modification and deletion)
import collections
import copy
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k == 0: return 0
        ans = 0
        lst_now = collections.deque()
        now = 1
        for i, value in enumerate(nums):
            if value >= k:
                now = 1
                lst_now = collections.deque()
            elif value * now >= k:
                while value * now >= k:
                    now /= lst_now.popleft()
                now *= value
                lst_now.append(value)
                # 包含value的子数组数目为 len(lst_now)
                ans += len(lst_now)
            else:
                now *= value
                lst_now.append(value)
                ans += len(lst_now)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


# test
def precesion_test():
    print("Precesion test")
    so = Solution()
    nums = [10, 5, 2, 6]
    k = 100
    print(8)


@profile(precision=8)
def speed_memory_test():
    print("\nSpeed and memory test")
    start = time.time()
    so = Solution()
    for _ in range(10000):
        pass
    print("Spend time:" + str(int((time.time() - start) * 1000)) + "ms")


# end test

def test():
    precesion_test()
    speed_memory_test()


if __name__ == "__main__":
    test()
