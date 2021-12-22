# 给定两个字符串 a 和 b，寻找重复叠加字符串 a 的最小次数，使得字符串 b 成为叠加后的字符串 a 的子串，如果不存在则返回 -1。 
# 
#  注意：字符串 "abc" 重复叠加 0 次是 ""，重复叠加 1 次是 "abc"，重复叠加 2 次是 "abcabc"。 
# 
#  
# 
#  示例 1： 
# 
#  输入：a = "abcd", b = "cdabcdab"
# 输出：3
# 解释：a 重复叠加三遍后为 "abcdabcdabcd", 此时 b 是其子串。
#  
# 
#  示例 2： 
# 
#  输入：a = "a", b = "aa"
# 输出：2
#  
# 
#  示例 3： 
# 
#  输入：a = "a", b = "a"
# 输出：1
#  
# 
#  示例 4： 
# 
#  输入：a = "abc", b = "wxyz"
# 输出：-1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= a.length <= 10⁴ 
#  1 <= b.length <= 10⁴ 
#  a 和 b 由小写英文字母组成 
#  
#  Related Topics 字符串 字符串匹配 👍 180 👎 0
import math
from functools import reduce
from itertools import product


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def repeatedStringMatch(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if b == "": return 0
        l1, l2 = len(a), len(b)
        num_a = int(math.ceil(l2 / l1))
        c = a * (num_a + 1)
        for i in range(l1,-1,-1):
            if c[i:i + l2] == b:
                return num_a + 1 if i != l1 else num_a
        else:
            return -1
# leetcode submit region end(Prohibit modification and deletion)

so = Solution()
a = "abc"
b="cabcabca"
print(so.repeatedStringMatch(a, b))
