# 你正在参加一个多角色游戏，每个角色都有两个主要属性：攻击 和 防御 。给你一个二维整数数组 properties ，其中 properties[i] = [
# attacki, defensei] 表示游戏中第 i 个角色的属性。 
# 
#  如果存在一个其他角色的攻击和防御等级 都严格高于 该角色的攻击和防御等级，则认为该角色为 弱角色 。更正式地，如果认为角色 i 弱于 存在的另一个角色 
# j ，那么 attackj > attacki 且 defensej > defensei 。 
# 
#  返回 弱角色 的数量。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：properties = [[5,5],[6,3],[3,6]]
# 输出：0
# 解释：不存在攻击和防御都严格高于其他角色的角色。
#  
# 
#  示例 2： 
# 
#  
# 输入：properties = [[2,2],[3,3]]
# 输出：1
# 解释：第一个角色是弱角色，因为第二个角色的攻击和防御严格大于该角色。
#  
# 
#  示例 3： 
# 
#  
# 输入：properties = [[1,5],[10,4],[4,3]]
# 输出：1
# 解释：第三个角色是弱角色，因为第二个角色的攻击和防御严格大于该角色。
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= properties.length <= 10⁵ 
#  properties[i].length == 2 
#  1 <= attacki, defensei <= 10⁵ 
#  
#  Related Topics 栈 贪心 数组 排序 单调栈 👍 48 👎 0


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
    def numberOfWeakCharacters(self, properties):
        """
        :type properties: List[List[int]]
        :rtype: int
        """
        res = 0
        properties.sort(key=lambda x: -min(x[0], x[1]))
        now_max0, now_max1 = properties[0][0], properties[0][1]
        pre_min = float('inf')
        pre_max0, pre_max1 = float('inf'), float('inf')
        for i in range(1,len(properties)):
            now_min = min(properties[i][0], properties[i][1])
            if now_min < pre_min:
                pre_max0, pre_max1 = now_max0, now_max1
                pre_min = now_min

            if properties[i][0] < pre_max0 and properties[i][1] < pre_max1:
                res += 1
            else:
                now_max0, now_max1 = max(properties[i][0], now_max0), max(properties[i][1], now_max1)
        return res


# leetcode submit region end(Prohibit modification and deletion)

so = Solution()
properties = [[8, 1], [5, 10], [5, 8], [10, 6], [1, 6], [10, 1]]
print(so.numberOfWeakCharacters(properties))
print(2)

print(so.numberOfWeakCharacters([[5, 5], [6, 3], [3, 6]]))
print(0)

print(so.numberOfWeakCharacters([[2, 2], [3, 3]]))
print(1)

print(so.numberOfWeakCharacters([[1, 5], [10, 4], [4, 3]]))
print(1)
