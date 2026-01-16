class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # prefix = [0]
        # count =0
        # for x in nums:
        #     prefix.append(prefix[-1]+x)
        # for i in range(len(nums)):
        #     for j in range(i,len(nums)):
        #         summ= prefix[j+1]-prefix[i]
        #         if summ ==k:
        #             count+=1
        # return count
        #use hashmap plus prefix
        prefix = 0
        freq = {0:1}
        count = 0
        #sum[i..j] = prefix[j+1]-prefix[i]
        #k = prefix[j+1]-prefix[i]
        #prefix[i] = prefix[j+1] - k
        for x in nums:
            prefix+=x
            need = prefix - k
            count+= freq.get(need,0)
            freq[prefix] =freq.get(prefix,0)+1
        return count
        


        