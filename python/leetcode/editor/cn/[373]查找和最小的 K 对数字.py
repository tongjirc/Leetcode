# 给定两个以 升序排列 的整数数组 nums1 和 nums2 , 以及一个整数 k 。 
# 
#  定义一对值 (u,v)，其中第一个元素来自 nums1，第二个元素来自 nums2 。 
# 
#  请找到和最小的 k 个数对 (u1,v1), (u2,v2) ... (uk,vk) 。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
# 输出: [1,2],[1,4],[1,6]
# 解释: 返回序列中的前 3 对数：
#      [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
#  
# 
#  示例 2: 
# 
#  
# 输入: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
# 输出: [1,1],[1,1]
# 解释: 返回序列中的前 2 对数：
#      [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
#  
# 
#  示例 3: 
# 
#  
# 输入: nums1 = [1,2], nums2 = [3], k = 3 
# 输出: [1,3],[2,3]
# 解释: 也可能序列中所有的数对都被返回:[1,3],[2,3]
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= nums1.length, nums2.length <= 10⁵ 
#  -10⁹ <= nums1[i], nums2[i] <= 10⁹ 
#  nums1 和 nums2 均为升序排列 
#  1 <= k <= 1000 
#  
#  Related Topics 数组 堆（优先队列） 👍 296 👎 0


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
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        l1, l2 = len(nums1), len(nums2)
        max_length = l1 * l2
        if k >= max_length:return [[i,j] for i in nums1 for j in nums2]
        lst_num = [1]
        rt_lst = [[nums1[0],nums2[0]]]
        i = 1
        while i < k:
            

# leetcode submit region end(Prohibit modification and deletion)

so = Solution()
nums1 = [1, 2]
nums2 = [3]
k = 3
# 输出: [1,3],[2,3]
