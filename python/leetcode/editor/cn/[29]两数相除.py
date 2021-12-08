# 给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。 
# 
#  返回被除数 dividend 除以除数 divisor 得到的商。 
# 
#  整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2 
# 
#  
# 
#  示例 1: 
# 
#  输入: dividend = 10, divisor = 3
# 输出: 3
# 解释: 10/3 = truncate(3.33333..) = truncate(3) = 3 
# 
#  示例 2: 
# 
#  输入: dividend = 7, divisor = -3
# 输出: -2
# 解释: 7/-3 = truncate(-2.33333..) = -2 
# 
#  
# 
#  提示： 
# 
#  
#  被除数和除数均为 32 位有符号整数。 
#  除数不为 0。 
#  假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2³¹, 231 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。 
#  
#  Related Topics 位运算 数学 👍 743 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend==0:return 0
        minus=(dividend*divisor<0)
        dividend,divisor=abs(dividend),abs(divisor)
        left,right=0,dividend
        while left<right:
            mid=left+(right-left)//2
            if mid*divisor==dividend:
                return mid if not minus else -mid
            elif mid*divisor>dividend:
                if (mid-1)*divisor<dividend:
                    return mid-1  if not minus else -(mid-1)
                right=mid-1
            else:
                if (mid+1)*divisor>dividend:
                    return mid  if not minus else -mid
                left=mid+1
        return right  if not minus else -right
# leetcode submit region end(Prohibit modification and deletion)

so=Solution()
print(so.divide(-2147483648,-1))