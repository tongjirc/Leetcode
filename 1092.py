# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 22:33:19 2020

@author: AlvinChen
"""

class Solution1:
    def shortestCommonSupersequence(self, a, b):
        if a in b:
            return b
        if b in a:
            return a
        allen,bllen=0,0
        aN,bN=len(a),len(b)
        for i in range(min(aN,bN)):
            if a[aN-i:]==b[0:i]:
                allen=i
            if b[bN-i:]==a[0:i]:
                bllen=i
        if allen>bllen:
            strout=a+b[allen:]
        else:
            strout=b+a[bllen:]
        return strout

class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        m = len(str1)
        n = len(str2)

        dp = [[''] * (n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + str1[i-1]
                else:
                    if len(dp[i-1][j]) > len(dp[i][j-1]):
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = dp[i][j-1]

        i = 0
        j = 0
        lcs = dp[m][n]
        ans = ''
        for cur_char in lcs:
            while(i < m and str1[i] != cur_char):
                ans += str1[i]
                i += 1
            while(j < n and str2[j] != cur_char):
                ans += str2[j]
                j += 1

            ans += cur_char
            i += 1
            j += 1
        # 可能有尾部字符没有在LCS里，在这里加上
        return ans + str1[i:] + str2[j:]

if __name__=="__main__":
	s=Solution()
	a,b=input(),input()
	print(s.shortestCommonSupersequence(a,b))
