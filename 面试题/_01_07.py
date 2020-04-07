# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 09:48:31 2020

@author: AlvinChen
"""

import numpy as np
class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        N=len(matrix)
        if N==0:
            return matrix
        copy=np.rot90(np.matrix(matrix),-1).tolist()
        matrix[:] = copy


if __name__=="__main__":
    try:
        s=Solution()
        matrix= eval(input())
        print(s.rotate(matrix))
    except Exception as e:
        print(e)