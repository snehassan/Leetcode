class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        for x in nums:
            freq[x] = freq.get(x,0) + 1
        maxi = max(freq.values()) 
        for k,v in freq.items():
            if v == maxi:
                return k
        