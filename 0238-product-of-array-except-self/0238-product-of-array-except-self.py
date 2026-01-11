class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # initialize with 1, the full array
        # loop over prefix of each i
        # loop over each suffix
        n = len(nums)
        ans = [1] * n

        # prefix products
        prefix = 1
        for i in range(n):
            ans[i] = prefix
            prefix *= nums[i]

        # suffix products
        suffix = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]

        return ans
            
            


        