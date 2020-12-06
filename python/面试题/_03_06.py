# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 00:05:28 2020

@author: AlvinChen
"""

class AnimalShelf:

    def __init__(self):
        self.cat=[]
        self.dog=[]
        self.catanddog=[]

    def enqueue(self, animal: List[int]) -> None:
        self.catanddog.append(animal[0])
        if animal[1]==0:
            self.cat.append(animal[0])
        else:
            self.dog.append(animal[0])

    def dequeueAny(self) -> List[int]:
        if self.catanddog:
            num=self.catanddog.pop(0)
            if num in self.cat:
                self.cat.remove(num)
                return([num,0])
            else:
                self.dog.remove(num)
                return([num,1])
        else:
            return([-1,-1])

    def dequeueDog(self) -> List[int]:
        if self.dog:
            num=self.dog.pop(0)
            self.catanddog.remove(num)
            return([num,1])
        else:
            return([-1,-1])
    def dequeueCat(self) -> List[int]:
        if self.cat:
            num=self.cat.pop(0)
            self.catanddog.remove(num)
            return([num,0])
        else:
            return([-1,-1])


# Your AnimalShelf object will be instantiated and called as such:
# obj = AnimalShelf()
# obj.enqueue(animal)
# param_2 = obj.dequeueAny()
# param_3 = obj.dequeueDog()
# param_4 = obj.dequeueCat()