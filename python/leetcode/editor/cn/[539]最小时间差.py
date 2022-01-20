# 给定一个 24 小时制（小时:分钟 "HH:MM"）的时间列表，找出列表中任意两个时间的最小时间差并以分钟数表示。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：timePoints = ["23:59","00:00"]
# 输出：1
#  
# 
#  示例 2： 
# 
#  
# 输入：timePoints = ["00:00","23:59","00:00"]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= timePoints.length <= 2 * 10⁴ 
#  timePoints[i] 格式为 "HH:MM" 
#  
#  Related Topics 数组 数学 字符串 排序 👍 157 👎 0


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
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        if len(timePoints) > 1440: return 0
        MAXTIME = 24 * 60
        for i in range(len(timePoints)):
            timePoints[i] = int(timePoints[i][:2]) * 60 + int(timePoints[i][3:])
        timePoints.sort()
        min_time_interval_minutes = (timePoints[0] - timePoints[-1]) % MAXTIME
        for i in range(1, len(timePoints)):
            interval = min(timePoints[i] - timePoints[i - 1], MAXTIME - (timePoints[i] - timePoints[i - 1]))
            if interval < min_time_interval_minutes:
                min_time_interval_minutes = interval
        return min_time_interval_minutes


# leetcode submit region end(Prohibit modification and deletion)

so = Solution()
timePoints = ["23:59", "00:00"]
print(so.findMinDifference((timePoints)))
print(1)

timePoints = ["00:00", "23:59", "00:00"]
print(so.findMinDifference((timePoints)))
print(0)
