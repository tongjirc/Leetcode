# 累加数 是一个字符串，组成它的数字可以形成累加序列。 
# 
#  一个有效的 累加序列 必须 至少 包含 3 个数。除了最开始的两个数以外，字符串中的其他数都等于它之前两个数相加的和。 
# 
#  给你一个只包含数字 '0'-'9' 的字符串，编写一个算法来判断给定输入是否是 累加数 。如果是，返回 true ；否则，返回 false 。 
# 
#  说明：累加序列里的数 不会 以 0 开头，所以不会出现 1, 2, 03 或者 1, 02, 3 的情况。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入："112358"
# 输出：true 
# 解释：累加序列为: 1, 1, 2, 3, 5, 8 。1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
#  
# 
#  示例 2： 
# 
#  
# 输入："199100199"
# 输出：true 
# 解释：累加序列为: 1, 99, 100, 199。1 + 99 = 100, 99 + 100 = 199 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= num.length <= 35 
#  num 仅由数字（0 - 9）组成 
#  
# 
#  
# 
#  进阶：你计划如何处理由过大的整数输入导致的溢出? 
#  Related Topics 字符串 回溯 👍 282 👎 0


from functools import reduce
from itertools import product


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        length = len(num)
        if length < 3: return False
        for len_first_num in range(1, length // 2 + 1):
            if num[0] == '0' and len_first_num != 1: continue
            num_first = int(num[:len_first_num])
            for len_second_num in range(1, min((length - len_first_num) // 2, length - 2 * len_first_num) + 1):
                if num[len_first_num] == '0' and len_second_num != 1: break
                num_second = int(num[len_first_num:len_first_num + len_second_num])
                remain_num = num[len_first_num + len_second_num:]
                if remain_num[0] == '0' and len_first_num != 1 and len_second_num != 1: continue
                first,second=num_first,num_second
                while remain_num != '':
                    str_second = str(first + second)
                    if remain_num.find(str_second) == 0:
                        remain_num = remain_num[len(str_second):]
                        first, second = second, int(str_second)
                    else:
                        break
                else:
                    return True
        return False


# leetcode submit region end(Prohibit modification and deletion)

so = Solution()
num = "111122335588143"
print(so.isAdditiveNumber(num))
# print(so.isAdditiveNumber("112358"))
# print(so.isAdditiveNumber("1"))
# print(so.isAdditiveNumber("199100199"))
# print(so.isAdditiveNumber("11112"))
# print(so.isAdditiveNumber("121121242"))
# print(so.isAdditiveNumber("121121243"))
# print(so.isAdditiveNumber("101"))
# print(so.isAdditiveNumber("000"))
# print(so.isAdditiveNumber("011"))
# print(so.isAdditiveNumber("00000000"))
