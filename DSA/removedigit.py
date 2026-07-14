class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        res=[]
        for i in range(len(number)):
            if number[i]==digit:
                t=number[0:i]+number[(i+1):]
                res.append(t)
        return max(res)        
