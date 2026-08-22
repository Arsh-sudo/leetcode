import math
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        pro=math.prod(int(digit) for digit in str(n))
        sum=0
        sn=str(n)
        for i in range(len(sn)):
            sum+=int(sn[i])
        if n%(sum+pro)==0:
            return True
        else:
            return False
        
        