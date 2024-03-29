# 给你一个整数 n，请你帮忙统计一下我们可以按下述规则形成多少个长度为 n 的字符串： 
# 
#  
#  字符串中的每个字符都应当是小写元音字母（'a', 'e', 'i', 'o', 'u'） 
#  每个元音 'a' 后面都只能跟着 'e' 
#  每个元音 'e' 后面只能跟着 'a' 或者是 'i' 
#  每个元音 'i' 后面 不能 再跟着另一个 'i' 
#  每个元音 'o' 后面只能跟着 'i' 或者是 'u' 
#  每个元音 'u' 后面只能跟着 'a' 
#  
# 
#  由于答案可能会很大，所以请你返回 模 10^9 + 7 之后的结果。 
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 1
# 输出：5
# 解释：所有可能的字符串分别是："a", "e", "i" , "o" 和 "u"。
#  
# 
#  示例 2： 
# 
#  输入：n = 2
# 输出：10
# 解释：所有可能的字符串分别是："ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" 和 "ua"。
#  
# 
#  示例 3： 
# 
#  输入：n = 5
# 输出：68 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 2 * 10^4 
#  
#  Related Topics 动态规划 👍 128 👎 0


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
    def countVowelPermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
# leetcode submit region end(Prohibit modification and deletion)

so=Solution()