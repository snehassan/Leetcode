class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # # initialize with 1, the full array
        # # loop over prefix of each i
        # # loop over each suffix
        # n = len(nums)
        # ans = [1] * n

        # # prefix products
        # prefix = 1
        # for i in range(n):
        #     ans[i] = prefix
        #     prefix *= nums[i]

        # # suffix products
        # suffix = 1
        # for i in range(n - 1, -1, -1):
        #     ans[i] *= suffix
        #     suffix *= nums[i]

        # return ans

        n = len(nums)
        output = [1]*n
        left_pr = right_pr = 1
        for i in range(n):
            output[i] *= left_pr
            left_pr*= nums[i]
            output[~i]*=right_pr
            right_pr*=nums[~i]
        return output
            
            


        