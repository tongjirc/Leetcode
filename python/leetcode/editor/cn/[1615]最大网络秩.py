# n 座城市和一些连接这些城市的道路 roads 共同组成一个基础设施网络。每个 roads[i] = [ai, bi] 都表示在城市 ai 和 bi 之间有
# 一条双向道路。 
# 
#  两座不同城市构成的 城市对 的 网络秩 定义为：与这两座城市 直接 相连的道路总数。如果存在一条道路直接连接这两座城市，则这条道路只计算 一次 。 
# 
#  整个基础设施网络的 最大网络秩 是所有不同城市对中的 最大网络秩 。 
# 
#  给你整数 n 和数组 roads，返回整个基础设施网络的 最大网络秩 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]
# 输出：4
# 解释：城市 0 和 1 的网络秩是 4，因为共有 4 条道路与城市 0 或 1 相连。位于 0 和 1 之间的道路只计算一次。
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：n = 5, roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
# 输出：5
# 解释：共有 5 条道路与城市 1 或 2 相连。
#  
# 
#  示例 3： 
# 
#  
# 输入：n = 8, roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
# 输出：5
# 解释：2 和 5 的网络秩为 5，注意并非所有的城市都需要连接起来。
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= n <= 100 
#  0 <= roads.length <= n * (n - 1) / 2 
#  roads[i].length == 2 
#  0 <= ai, bi <= n-1 
#  ai != bi 
#  每对城市之间 最多只有一条 道路相连 
#  
#  Related Topics 图 👍 18 👎 0

class RouteTree:
    def __init__(self, val):
        self.val = val
        self.trans = []


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
        return str(self.ListNode2Lst(self))

    def ListNode2Lst(self, node):
        Lst = []
        while node:
            Lst.append(node.val)
            node = node.next
        return Lst

    def Lst2ListNode(self, Lst):
        dummy = ListNode(-1, None)
        rcd = dummy
        for i in Lst:
            nd = ListNode(i, None)
            dummy.next = nd
            dummy = dummy.next
        return rcd.next


class TreeNode:
    def __init__(self):
        self.val = None
        self.left = None
        self.right = None


from functools import reduce
from itertools import product


# leetcode submit region begin(Prohibit modification and deletion)
import collections
class Solution(object):
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        if roads == []: return 0
        city_count = collections.defaultdict(int)
        for road in roads:
            city_count[road[0]] += 1
            city_count[road[1]] += 1
        ans = 0
        lst_sorted_city = sorted(city_count.items(),key=lambda x: x[1])
        for i in range(len(lst_sorted_city) - 1, 0, -1):
            if lst_sorted_city[i][1] + lst_sorted_city[i - 1][1] < ans:
                break
            for j in range(i - 1, -1, -1):
                connection = lst_sorted_city[i][1] + lst_sorted_city[j][1]
                if connection < ans:
                    break
                if [lst_sorted_city[i][0], lst_sorted_city[j][0]] in roads or [lst_sorted_city[j][0],
                                                                         lst_sorted_city[i][0]] in roads:
                    connection -= 1
                ans = max(connection, ans)
        return ans


# leetcode submit region end(Prohibit modification and deletion)

so = Solution()
n, roads = 8, [[0, 1], [1, 2], [2, 3], [2, 4], [5, 6], [5, 7]]
print(so.maximalNetworkRank(n,roads))
