class Solution:
    def firstUniqChar(self, s: str) -> int:
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i,x in enumerate(s):
            if d[x]==1:
                return i
        return -1