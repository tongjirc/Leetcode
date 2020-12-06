# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 00:23:42 2020

@author: AlvinChen
"""
class Solution1:
    def findLadders(self, begin, end, wordlist):
        """
        input:str,str,List[str]
        output:List[List[str]]
        beyond time limit
        """
        wholelst=[]
        if not wordlist or end not in wordlist:return wholelst
        wl=len(wordlist[0])
        if begin not in wordlist:bwordLst=wordlist+[begin]
        else:bwordLst=wordlist
        neighbor={}

        for i in range(0,len(bwordLst)):
            neighbor.setdefault(bwordLst[i],[set(),False])
            for j in range(i+1,len(bwordLst)):
                count=0
                for k in range(wl):
                    if bwordLst[i][k]!=bwordLst[j][k]:
                        count+=1
                        if count>=2:break
                else:
                    neighbor.setdefault(bwordLst[i],[set(),False])[0].add(bwordLst[j])
                    neighbor.setdefault(bwordLst[j],[set(),False])[0].add(bwordLst[i])

        bfslst=[[begin,0,[begin]]]
        finddeep=None
        while bfslst:
            node,deep,lst=bfslst.pop(0)
            if finddeep!=None and finddeep!=deep:break
            if node==end:
                finddeep=deep
                wholelst.append(lst)
            else :
                for i in neighbor[node][0]:
                    bfslst.append([i,deep+1,lst+[i]])
        return wholelst

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList.append(beginWord)
        ### 构建具有邻接关系的桶
        buckets = defaultdict(list)
        for word in wordList:
            for i in range(len(beginWord)):
                match = word[:i] + '_' + word[i+1:]
                buckets[match].append(word)
        ##### BFS遍历
        preWords = defaultdict(list)#前溯词列表
        toSeen = deque([(beginWord, 1)])#待遍历词及深度列表
        beFound = {beginWord:1}#已探测词词列表
        while toSeen:
            curWord, level = toSeen.popleft()
            for i in range(len(beginWord)):
                match = curWord[:i] + '_' + curWord[i+1:]
                for word in buckets[match]:
                    if word not in beFound:
                        beFound[word] = level+1
                        toSeen.append((word, level+1))
                    if beFound[word] == level+1:#当前深度等于该词首次遍历深度，则仍应加入前溯词列表
                        preWords[word].append(curWord)
            if endWord in beFound and level+1 > beFound[endWord]:#已搜索到目标词，且完成当前层遍历
                break
        #### 列表推导式输出结果
        if endWord in beFound:
            res = [[endWord]]
            while res[0][0] != beginWord:
                res = [[word] + r for r in res for word in preWords[r[0]]]
            return res
        else:
            return []

if __name__=="__main__":
    s=Solution()
    begin,end,wordlist=eval(input()),eval(input()),eval(input())
    print(s.findLadders(begin,end,wordlist))