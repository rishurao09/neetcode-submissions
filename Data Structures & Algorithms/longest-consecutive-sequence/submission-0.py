class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett  = set(nums)
        ln = 0 
        for i in sett : 
            if i - 1 not in sett : 
                lg = 1 
                while i + lg in sett : 
                    lg += 1 
                ln = max(ln,lg)
        return ln 