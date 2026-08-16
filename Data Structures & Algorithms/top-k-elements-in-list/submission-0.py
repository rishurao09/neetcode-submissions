class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        for i in nums : 
            mp[i] = mp.get(i,0)+1 
        sr = sorted(mp.keys(), key = lambda x : mp[x], reverse =True)
        return sr[:k]
