import collections
class Solution:
    def compressString(self, S):
        ans=""
        last=""
        count=0
        i=0
        while i<len(S):
            ans+=S[i]
            i+=1
            count+=1
            if i==len(S) or S[i]!=ans[-1]:
                last+=ans[-1]
                last+=str(count)
                count=0
        if len(last)>=len(S):
            last=S
        return last


if __name__=="__main__":
	s=Solution()
	nums=eval(input())
	print(s.compressString(nums))

