class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(nums)-1

        def RBinS(l,h,target):
            if (l > h):
                return l
            mid = (l+h)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                return RBinS(l,mid-1,target)
            else:
                return RBinS(mid+1,h,target)
        return RBinS(0, len(nums)-1, target)