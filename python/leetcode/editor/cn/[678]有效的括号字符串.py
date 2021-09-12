# 给定一个只包含三种字符的字符串：（ ，） 和 *，写一个函数来检验这个字符串是否为有效字符串。有效字符串具有如下规则： 
# 
#  
#  任何左括号 ( 必须有相应的右括号 )。 
#  任何右括号 ) 必须有相应的左括号 ( 。 
#  左括号 ( 必须在对应的右括号之前 )。 
#  * 可以被视为单个右括号 ) ，或单个左括号 ( ，或一个空字符串。 
#  一个空字符串也被视为有效字符串。 
#  
# 
#  示例 1: 
# 
#  
# 输入: "()"
# 输出: True
#  
# 
#  示例 2: 
# 
#  
# 输入: "(*)"
# 输出: True
#  
# 
#  示例 3: 
# 
#  
# 输入: "(*))"
# 输出: True
#  
# 
#  注意: 
# 
#  
#  字符串大小将在 [1，100] 范围内。 
#  
#  Related Topics 栈 贪心 字符串 动态规划 👍 305 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def checkValidString(self, s: str) -> bool:
        length=len(s)
        def newstack(n,left):
            if left<0 or left>length-n:return False
            for i in range(n,length):
                if s[i]=='(':
                    left+=1
                elif s[i]==')':
                    if left>0:
                        left-=1
                    else:
                        return False
                else:
                    return newstack(i+1,left-1) or newstack(i+1,left) or newstack(i+1,left+1)
            return True if left==0 else False

        starNum=[]
        leftNum=[]
        for i in range(len(s)):
            if s[i]=='(':
                leftNum.append(i)
            elif s[i]=='*':
                starNum.append(i)
            else:
                if leftNum:
                    leftNum.pop()
                elif starNum:
                    starNum.pop()
                else:
                    return False
        if len(leftNum)<=len(starNum):
            while leftNum:
                if not starNum.pop()>leftNum.pop():
                    return False
            return True
        else:
            return False

        return newstack(0,0)
# leetcode submit region end(Prohibit modification and deletion)
