# 给你一个 m x n 的整数网格 accounts ，其中 accounts[i][j] 是第 i 位客户在第 j 家银行托管的资产数量。返回最富有客户所拥
# 有的 资产总量 。 
# 
#  客户的 资产总量 就是他们在各家银行托管的资产数量之和。最富有客户就是 资产总量 最大的客户。 
# 
#  
# 
#  示例 1： 
# 
#  输入：accounts = [[1,2,3],[3,2,1]]
# 输出：6
# 解释：
# 第 1 位客户的资产总量 = 1 + 2 + 3 = 6
# 第 2 位客户的资产总量 = 3 + 2 + 1 = 6
# 两位客户都是最富有的，资产总量都是 6 ，所以返回 6 。
#  
# 
#  示例 2： 
# 
#  输入：accounts = [[1,5],[7,3],[3,5]]
# 输出：10
# 解释：
# 第 1 位客户的资产总量 = 6
# 第 2 位客户的资产总量 = 10 
# 第 3 位客户的资产总量 = 8
# 第 2 位客户是最富有的，资产总量是 10 
# 
#  示例 3： 
# 
#  输入：accounts = [[2,8,7],[7,1,3],[1,9,5]]
# 输出：17
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == accounts.length 
#  n == accounts[i].length 
#  1 <= m, n <= 50 
#  1 <= accounts[i][j] <= 100 
#  
#  Related Topics 数组 矩阵 👍 80 👎 0


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
        
import time
from functools import reduce
from itertools import product
from memory_profiler import profile

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        return max(map(sum,accounts))
# leetcode submit region end(Prohibit modification and deletion)


# test
def precesion_test():
    print("Precesion test")
    so = Solution()


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


