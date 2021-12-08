# 给定一个字符串数组 words，找到 length(word[i]) * length(word[j]) 的最大值，并且这两个单词不含有公共字母。你可以认为
# 每个单词只包含小写字母。如果不存在这样的两个单词，返回 0。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: ["abcw","baz","foo","bar","xtfn","abcdef"]
# 输出: 16 
# 解释: 这两个单词为 "abcw", "xtfn"。 
# 
#  示例 2: 
# 
#  
# 输入: ["a","ab","abc","d","cd","bcd","abcd"]
# 输出: 4 
# 解释: 这两个单词为 "ab", "cd"。 
# 
#  示例 3: 
# 
#  
# 输入: ["a","aa","aaa","aaaa"]
# 输出: 0 
# 解释: 不存在这样的两个单词。
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= words.length <= 1000 
#  1 <= words[i].length <= 1000 
#  words[i] 仅包含小写字母 
#  
#  Related Topics 位运算 数组 字符串 👍 227 👎 0

from functools import reduce
from itertools import product

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxProduct1(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        def intersection(str1,str2):
            if set(str1).intersection(set(str2)):
                return True
            return False
        sort_words=sorted(words,key=lambda x:len(x))
        max_length=0
        for i in range(len(words)-1,0,-1):
            if len(sort_words[i])*len(sort_words[i-1])<=max_length:
                break
            for j in range(len(words)-2,-1,-1):
                if len(sort_words[i])*len(sort_words[j])<=max_length:
                    break
                if intersection(sort_words[i],sort_words[j]):
                    continue
                else:
                    max_length=len(sort_words[i])*len(sort_words[j])
                    break
        return max_length
    def maxProduct(self, words: List[str]) -> int:
        masks = [reduce(lambda a, b: a | (1 << (ord(b) - ord('a'))), word, 0) for word in words]
        return max((len(x[1]) * len(y[1]) for x, y in product(zip(masks, words), repeat=2) if x[0] & y[0] == 0), default=0)


# leetcode submit region end(Prohibit modification and deletion)
so=Solution()
words=["a","aa","aaa","aaaa"]
print(so.maxProduct(words))