class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = 1
        ans = [1]*len(nums)
        for i in range(len(nums)): 
            ans[i] = l 
            l *= nums[i]
        r = 1
        for i in range(len(nums)-1,-1,-1):
            ans[i] *= r 
            r *= nums[i]
        return ans