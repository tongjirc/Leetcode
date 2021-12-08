# 给你一个字符串 s ，其中包含字母顺序打乱的用英文单词表示的若干数字（0-9）。按 升序 返回原始的数字。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "owoztneoer"
# 输出："012"
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "fviefuro"
# 输出："45"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 10⁵ 
#  s[i] 为 ["e","g","f","i","h","o","n","s","r","u","t","w","v","x","z"] 这些字符之一 
#  s 保证是一个符合题目要求的字符串 
#  
#  Related Topics 哈希表 数学 字符串 👍 129 👎 0


from functools import reduce
from itertools import product
# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        dict_key_word={1:"o",
                  2:"w",
                  3:"h",
                  4:"u",
                  5:"f",
                  6:"x",
                  7:"s",
                  8:"g",
                  9:"i",
                  0:"z"}
        lst_word=["e","g","f","i","h","o","n","s","r","u","t","w","v","x","z"]
        dict_num_word=dict(zip(lst_word,[0]*len(lst_word)))
        dict_num_num={1:"one",
                  2:"two",
                  3:"three",
                  4:"four",
                  5:"five",
                  6:"six",
                  7:"seven",
                  8:"eight",
                  9:"nine",
                  0:"zero"
                  }
        for item in dict_num_num.items():
            dict_num_i=dict_num_word.copy()
            for i in item[1]:
                dict_num_i[i]+=1
            dict_num_num[item[0]]=dict_num_i
        for i in s:
            dict_num_word[i]+=1
        ans=[0]*10

        def minus_num(num):
            total_num=dict_num_word[dict_key_word[num]]
            for i in dict_num_num[num]:
                if dict_num_num[num][i]>0:
                    dict_num_word[i]-=total_num
            ans[num]+=total_num
        # stage 1
        minus_num(0)
        minus_num(2)
        minus_num(4)
        minus_num(6)
        minus_num(8)
        # stage 2
        minus_num(1)
        minus_num(3)
        minus_num(5)
        # stage 3
        minus_num(7)
        minus_num(9)
        rts=""
        for i in range(10):
            rts+=str(i)*ans[i]
        return rts
# leetcode submit region end(Prohibit modification and deletion)

so=Solution()
s="owoztneoer"
print(so.originalDigits(s))