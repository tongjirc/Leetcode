# 你需要从空字符串开始 构造 一个长度为 n 的字符串 s ，构造的过程为每次给当前字符串 前面 添加 一个 字符。构造过程中得到的所有字符串编号为 1 到 
# n ，其中长度为 i 的字符串编号为 si 。 
# 
#  
#  比方说，s = "abaca" ，s1 == "a" ，s2 == "ca" ，s3 == "aca" 依次类推。 
#  
# 
#  si 的 得分 为 si 和 sn 的 最长公共前缀 的长度（注意 s == sn ）。 
# 
#  给你最终的字符串 s ，请你返回每一个 si 的 得分之和 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "babab"
# 输出：9
# 解释：
# s1 == "b" ，最长公共前缀是 "b" ，得分为 1 。
# s2 == "ab" ，没有公共前缀，得分为 0 。
# s3 == "bab" ，最长公共前缀为 "bab" ，得分为 3 。
# s4 == "abab" ，没有公共前缀，得分为 0 。
# s5 == "babab" ，最长公共前缀为 "babab" ，得分为 5 。
# 得分和为 1 + 0 + 3 + 0 + 5 = 9 ，所以我们返回 9 。 
# 
#  示例 2 ： 
# 
#  
# 输入：s = "azbazbzaz"
# 输出：14
# 解释：
# s2 == "az" ，最长公共前缀为 "az" ，得分为 2 。
# s6 == "azbzaz" ，最长公共前缀为 "azb" ，得分为 3 。
# s9 == "azbazbzaz" ，最长公共前缀为 "azbazbzaz" ，得分为 9 。
# 其他 si 得分均为 0 。
# 得分和为 2 + 3 + 9 = 14 ，所以我们返回 14 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 10⁵ 
#  s 只包含小写英文字母。 
#  
#  Related Topics 字符串 二分查找 字符串匹配 后缀数组 哈希函数 滚动哈希 👍 21 👎 0


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
    def sumScores(self, s):
        """
        :type s: str
        :rtype: int
        """
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


