# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 10:50:58 2020

@author: AlvinChen
"""
class Solution:
    def minimumLengthEncoding(self, words):
        s=0
        indLst=[]
        for i in words:
            indLst.append(s)
            s=s+len(i)+1
        Lst="#".join(words)+"#"
        for i in range(len(words)):
            if Lst.find(words[i]+"#") != Lst.rfind(words[i]+"#"):
                Lst=Lst[0:indLst[i]]+"*"*(len(words[i])+1)+Lst[indLst[i]+len(words[i])+1:]
        finalLst=Lst.replace("*","")
        return len(finalLst)

class Solution1:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        good = set(words)
        for word in words:
            for k in range(1, len(word)):
                good.discard(word[k:])

        return sum(len(word) + 1 for word in good)

class Solution2:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = list(set(words)) #remove duplicates
        #Trie is a nested dictionary with nodes created
        # when fetched entries are missing
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()

        #reduce(..., S, trie) is trie[S[0]][S[1]][S[2]][...][S[S.length - 1]]
        nodes = [reduce(dict.__getitem__, word[::-1], trie)
                 for word in words]

        #Add word to the answer if it's node has no neighbors
        return sum(len(word) + 1
                   for i, word in enumerate(words)
                   if len(nodes[i]) == 0)

if __name__=="__main__":
    s=Solution()
    words=eval(input())
    print(s.minimumLengthEncoding(words))
