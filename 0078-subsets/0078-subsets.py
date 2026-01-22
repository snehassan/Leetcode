class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []

        def backtrack_recursive(i):
            if i == n:
                res. append(sol[:])
                return
            # we are not picking nums[i]

            backtrack_recursive(i+1)

            # we are picking
            sol.append(nums[i])
            backtrack_recursive(i+1)
            sol.pop()

        backtrack_recursive(0)
        return res