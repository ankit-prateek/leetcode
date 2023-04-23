class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        
        kLen = floor(log10(k)) + 1
        R = len(s)
        variants = [0] * R
        
        for L in reversed(range(R)):
            if s[L] == '0':
                variants[L] = 0  
            else:
                result = R - L <= kLen and int(s[L:R]) <= k

                for i in range(1, min(kLen, R-L)):
                    result += variants[L+i]
                    i += 1

                if kLen < R-L and int(s[L:L+kLen]) <= k:
                    result += variants[L+kLen]

                variants[L] = result % 1000000007
       
        return variants[0]