# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 00:05:28 2020

@author: AlvinChen
"""

class Solution:
    def intersection(self, p1,p2,p3,p4):
        x1,y1=p1
        x2,y2=p2
        x3,y3=p3
        x4,y4=p4
#        x1,y1=[0,3]
#        x2,y2=[0,6]
#        x3,y3=[0,1]
#        x4,y4=[0,5]
        if x1==x2 and x3==x4:
            if x2!=x3:
                return []
            else:
                y=sorted([y1,y2,y3,y4])
                if (y[0] in [y1,y2] and y[2] in [y1,y2]) or (y[0] in [y3,y4] and y[2] in [y3,y4]):
                    return [x1,y[1]]
                else:
                    return []
        elif x3==x4:
            x0=x3
            y0=((x0-x1)*(y2-y1))/(x2-x1)+y1
            if ((x1<=x0<=x2 or x2<=x0<=x1) and (y1<=y0<=y2 or y2<=y0<=y1)) and ((x3<=x0<=x4 or x4<=x0<=x3) and (y3<=y0<=y4 or y4<=y0<=y3)):
                return [x0,y0]
            else:
                return []
        elif x1==x2:
            x0=x1
            y0=((x0-x3)*(y4-y3)/(x4-x3)+y3)
            if ((x1<=x0<=x2 or x2<=x0<=x1) and (y1<=y0<=y2 or y2<=y0<=y1)) and ((x3<=x0<=x4 or x4<=x0<=x3) and (y3<=y0<=y4 or y4<=y0<=y3)):
                return [x0,y0]
            else:
                return []
        else:
            # coincident
            k1=(y2-y1)/(x2-x1)
            k2=(y4-y3)/(x4-x3)
            if k1==k2:
                if y1==((x1-x3)*(y4-y3))/(x4-x3)+y3:
                    x=sorted([x1,x2,x3,x4])
                    if (x[0] in [x1,x2] and x[2] in [x1,x2]) or (x[0] in [x3,x4] and x[2] in [x3,x4]):
                        x0=x[1]
                        y0=((x0-x3)*(y4-y3)/(x4-x3)+y3)
                        return [x0,y0]
                    else:
                        return []
                else:
                    return []
            else:
                # incoincident
                x0=(x3*(y4-y3)*(x2-x1)+y3*(x2-x1)-x1*(y2-y1)*(x4-x3)+y1*(x4-x3))/((y4-y3)*(x2-x1)-(y2-y1)*(x4-x3))
                y0=((x0-x3)*(y4-y3)/(x4-x3)+y3)
                if ((x1<=x0<=x2 or x2<=x0<=x1) and (y1<=y0<=y2 or y2<=y0<=y1)) and ((x3<=x0<=x4 or x4<=x0<=x3) and (y3<=y0<=y4 or y4<=y0<=y3)):
                    return [x0,y0]
                else:
                    return []


class Solution:
    def intersection(self, start1: List[int], end1: List[int], start2: List[int], end2: List[int]) -> List[float]:
        # 判断 (xk, yk) 是否在「线段」(x1, y1)~(x2, y2) 上
        # 这里的前提是 (xk, yk) 一定在「直线」(x1, y1)~(x2, y2) 上
        def inside(x1, y1, x2, y2, xk, yk):
            # 若与 x 轴平行，只需要判断 x 的部分
            # 若与 y 轴平行，只需要判断 y 的部分
            # 若为普通线段，则都要判断
            return (x1 == x2 or min(x1, x2) <= xk <= max(x1, x2)) and (y1 == y2 or min(y1, y2) <= yk <= max(y1, y2))

        def update(ans, xk, yk):
            # 将一个交点与当前 ans 中的结果进行比较
            # 若更优则替换
            return [xk, yk] if not ans or [xk, yk] < ans else ans

        x1, y1 = start1
        x2, y2 = end1
        x3, y3 = start2
        x4, y4 = end2

        ans = list()
        # 判断 (x1, y1)~(x2, y2) 和 (x3, y3)~(x4, y3) 是否平行
        if (y4 - y3) * (x2 - x1) == (y2 - y1) * (x4 - x3):
            # 若平行，则判断 (x3, y3) 是否在「直线」(x1, y1)~(x2, y2) 上
            if (y2 - y1) * (x3 - x1) == (y3 - y1) * (x2 - x1):
                # 判断 (x3, y3) 是否在「线段」(x1, y1)~(x2, y2) 上
                if inside(x1, y1, x2, y2, x3, y3):
                    ans = update(ans, x3, y3)
                # 判断 (x4, y4) 是否在「线段」(x1, y1)~(x2, y2) 上
                if inside(x1, y1, x2, y2, x4, y4):
                    ans = update(ans, x4, y4)
                # 判断 (x1, y1) 是否在「线段」(x3, y3)~(x4, y4) 上
                if inside(x3, y3, x4, y4, x1, y1):
                    ans = update(ans, x1, y1)
                # 判断 (x2, y2) 是否在「线段」(x3, y3)~(x4, y4) 上
                if inside(x3, y3, x4, y4, x2, y2):
                    ans = update(ans, x2, y2)
            # 在平行时，其余的所有情况都不会有交点
        else:
            # 联立方程得到 t1 和 t2 的值
            t1 = (x3 * (y4 - y3) + y1 * (x4 - x3) - y3 * (x4 - x3) - x1 * (y4 - y3)) / ((x2 - x1) * (y4 - y3) - (x4 - x3) * (y2 - y1))
            t2 = (x1 * (y2 - y1) + y3 * (x2 - x1) - y1 * (x2 - x1) - x3 * (y2 - y1)) / ((x4 - x3) * (y2 - y1) - (x2 - x1) * (y4 - y3))
            # 判断 t1 和 t2 是否均在 [0, 1] 之间
            if 0.0 <= t1 <= 1.0 and 0.0 <= t2 <= 1.0:
                ans = [x1 + t1 * (x2 - x1), y1 + t1 * (y2 - y1)]

        return ans

if __name__=="__main__":
    p1=eval(input())
    p2=eval(input())
    p3=eval(input())
    p4=eval(input())
    s=Solution()
    print(s.intersection(p1,p2,p3,p4))
