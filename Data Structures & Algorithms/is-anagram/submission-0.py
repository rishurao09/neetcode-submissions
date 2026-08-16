class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smp = {}
        tmp = {}
        for i in s : 
            smp[i] = smp.get(i,0) + 1 
        for r in t : 
            tmp[r] = tmp.get(r,0) + 1 
        if tmp == smp : 
            return True 
        return False