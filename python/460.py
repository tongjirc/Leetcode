# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 08:59:40 2020

@author: AlvinChen
"""
class LFUCache1:

    def __init__(self, capacity: int):
         self.c=capacity
         self.lst=[]

    def get(self, key: int) -> int:
        n=0
        readylst=[]
        while self.lst and n<self.c:
            readylst.append(self.lst.pop())
            n+=1
            if readylst[-1][0]==key:
                out=readylst.pop()
                while readylst:
                    self.lst.append(readylst.pop())
                self.lst.append(out)
                print(self.lst)
                return out[1]
        else:
            while readylst:
                self.lst.append(readylst.pop())
            print(self.lst)
            return -1


    def put(self, key: int, value: int) -> None:
        self.lst.append((key,value,))

import collections
import time
class LFUCache:

    def __init__(self, capacity: int):
         self.c=capacity
         self.count=collections.Counter()
         self.dic={}
         self.timetable={}

    def get(self, key: int) -> int:
        if key in self.count:
            self.count[key]+=1
            self.timetable[key]=time.time()
            return self.dic[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if not key in self.count:
            if len(self.count)<self.c:
                self.count[key]=1
                self.dic[key]=value
                self.timetable[key]=time.time()
            elif self.c==0:
                return -1
            else:
                keylst=sorted(self.count,key=lambda item: self.count[item])
                #find time mini
                minilen,minilst=1,[keylst[0]]
                while minilen<self.c and self.count[keylst[minilen]]==self.count[keylst[minilen-1]]:
                    minilen+=1
                    minilst.append(keylst[minilen])
                minitime,minikey=inf,0
                for i in minilst:
                    if self.timetable[i]<minitime:
                        minitime=self.timetable[i]
                        minikey=i

                del self.count[minikey]
                del self.dic[minikey]
                self.count[key]=1
                self.dic[key]=value
                self.timetable[key]=time.time()
        else:
            self.count[key]+=1
            self.dic[key]=value
            self.timetable[key]=time.time()



if __name__=="__main__":
    try:
        cache = LFUCache( 3 )

        cache.put(2, 2)
        cache.put(1, 1)
        print("2",cache.get(2))
        print("1",cache.get(1))
        print("2",cache.get(2))
        cache.put(3, 3)
        cache.put(4, 4)
        print("-1",cache.get(3))
        print("2",cache.get(2))
        print("1",cache.get(1))
        print("4",cache.get(4))
    except Exception as e:
        print(e)