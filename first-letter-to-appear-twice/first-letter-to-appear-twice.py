class Solution:
    def repeatedCharacter(self, s: str) -> str:
        d=set()
        for i in s:
            if i not in d:
                d.add(i)
            else:
                return i