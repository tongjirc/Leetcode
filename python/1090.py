# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 09:51:09 2020

@author: AlvinChen
"""
class Solution:
    def largestValsFromLabels(self, values,labels,num_wanted,use_limit):
        maxnum=0
        if len(values)==0:
            return maxnum
        comb=sorted(zip(map(str,labels),values),key=lambda x:x[1],reverse=True)
        dic={}
        enddic={}
        for label,value in comb:
            if label in dic.keys():
                dic[label].append(value)
            else:
                dic[label]=[value]
                enddic[label]=[]
        num=0
        for label,value in comb:
            if num>=num_wanted:
                break
            if len(enddic[label])>=use_limit:
                continue
            else:
                enddic[label].append(value)
                num+=1
        for i in enddic.items():
            maxnum+=sum(i[1])
        return maxnum



if __name__=="__main__":
    try:
        a=Solution()
        values= eval(input())
        labels= eval(input())
        num_wanted,use_limit=eval(input()),eval(input())
        print(a.largestValsFromLabels(values,labels,num_wanted,use_limit))
    except Exception as e:
        print(e)