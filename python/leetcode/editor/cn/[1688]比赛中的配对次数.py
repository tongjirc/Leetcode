# 给你一个整数 n ，表示比赛中的队伍数。比赛遵循一种独特的赛制： 
# 
#  
#  如果当前队伍数是 偶数 ，那么每支队伍都会与另一支队伍配对。总共进行 n / 2 场比赛，且产生 n / 2 支队伍进入下一轮。 
#  如果当前队伍数为 奇数 ，那么将会随机轮空并晋级一支队伍，其余的队伍配对。总共进行 (n - 1) / 2 场比赛，且产生 (n - 1) / 2 + 1
#  支队伍进入下一轮。 
#  
# 
#  返回在比赛中进行的配对次数，直到决出获胜队伍为止。 
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 7
# 输出：6
# 解释：比赛详情：
# - 第 1 轮：队伍数 = 7 ，配对次数 = 3 ，4 支队伍晋级。
# - 第 2 轮：队伍数 = 4 ，配对次数 = 2 ，2 支队伍晋级。
# - 第 3 轮：队伍数 = 2 ，配对次数 = 1 ，决出 1 支获胜队伍。
# 总配对次数 = 3 + 2 + 1 = 6
#  
# 
#  示例 2： 
# 
#  输入：n = 14
# 输出：13
# 解释：比赛详情：
# - 第 1 轮：队伍数 = 14 ，配对次数 = 7 ，7 支队伍晋级。
# - 第 2 轮：队伍数 = 7 ，配对次数 = 3 ，4 支队伍晋级。 
# - 第 3 轮：队伍数 = 4 ，配对次数 = 2 ，2 支队伍晋级。
# - 第 4 轮：队伍数 = 2 ，配对次数 = 1 ，决出 1 支获胜队伍。
# 总配对次数 = 7 + 3 + 2 + 1 = 13
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 200 
#  
#  Related Topics 数学 模拟 👍 57 👎 0


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
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        return n-1
# leetcode submit region end(Prohibit modification and deletion)

so = Solution()