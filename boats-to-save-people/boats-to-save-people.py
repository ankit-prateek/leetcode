from bisect import bisect
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        d={}
        for i in people:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        people.sort()
        ans=0
        for i in range(len(people)-1,-1,-1):
            if d[people[i]]>0:
                d[people[i]]-=1
                t=limit-people[i]
                x=bisect(people,t)
                for j in range(x-1,-1,-1):
                    if people[j]>t:
                        continue
                    if d[people[j]]!=0:
                        d[people[j]]-=1
                        break

   
                ans+=1
        return ans
            

