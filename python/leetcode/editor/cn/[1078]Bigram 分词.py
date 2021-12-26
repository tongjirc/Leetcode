# 给出第一个词 first 和第二个词 second，考虑在某些文本 text 中可能以 "first second third" 形式出现的情况，其中 
# second 紧随 first 出现，third 紧随 second 出现。 
# 
#  对于每种这样的情况，将第三个词 "third" 添加到答案中，并返回答案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：text = "alice is a good girl she is a good student", first = "a", second = 
# "good"
# 输出：["girl","student"]
#  
# 
#  示例 2： 
# 
#  
# 输入：text = "we will we will rock you", first = "we", second = "will"
# 输出：["we","rock"]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= text.length <= 1000 
#  text 由小写英文字母和空格组成 
#  text 中的所有单词之间都由 单个空格字符 分隔 
#  1 <= first.length, second.length <= 10 
#  first 和 second 由小写英文字母组成 
#  
#  Related Topics 字符串 👍 39 👎 0


from functools import reduce
from itertools import product


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        text = text.strip(" ")
        text = " " + text
        equal = False
        if first == second: equal = True
        match = " " + first + " " + second + " "
        length_n, length_m = len(text), len(match)
        lst_kmp = [0] * length_m

        j = 0
        for i in range(1, length_m):
            while j > 0 and match[j] != match[i]:
                j = lst_kmp[j - 1]
            if match[j] == match[i]:
                j += 1
            lst_kmp[i] = j

        j = 0
        lst_match = []
        lst_rt = []
        for i in range(0, len(text)):
            while j > 0 and text[i] != match[j]:
                j = lst_kmp[j - 1]
            if match[j] == text[i]:
                j += 1
            if j == length_m:
                lst_match.append(i)
                j = 1
                if equal: j += len(first) + 1

        # 找到下一个单词
        for i in lst_match:
            k = 1
            while i + k < length_n and text[i + k] != " ":
                k += 1
            lst_rt.append(text[i + 1:i + k])
        return lst_rt


# leetcode submit region end(Prohibit modification and deletion)

so = Solution()
text = "alice is a good girl she is a good student"
first = "a"
second = "good"
print(so.findOcurrences(text, first, second))
print(["girl", "student"])

text = "we will we will rock you"
first = "we"
second = "will"
print(so.findOcurrences(text, first, second))
print(["we", "rock"])

text = "alice is aa good girl she is a good student"
first = "a"
second = "good"
print(so.findOcurrences(text, first, second))
print(["student"])

text = "we we we we will rock you"
first = "we"
second = "we"
print(so.findOcurrences(text, first, second))
print(["we", "we", "will"])
