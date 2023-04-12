class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d={
            "b":0,
            "a":0,
            "l":0,
            "o":0,
            "n":0
        }
        for i in text:
            if i in "balon":
                d[i]+=1
        return min([
            d["b"],
            d["a"],
            d["l"]//2,
            d["o"]//2,
            d["n"],
        ])

        