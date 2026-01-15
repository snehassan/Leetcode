class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count = {}
        result = []
        for x in p:
            p_count[x] = p_count.get(x,0)+1
        print(p_count)
        l = 0
        window_count = {}
        for r in range(len(s)):
            temp = s[r]
            window_count[temp] = window_count.get(temp,0)+1
            if r-l+1>len(p):
                left_char = s[l]
                window_count[left_char]-=1
                if window_count[left_char] ==0:
                    del window_count[left_char]
                l+=1
            if window_count == p_count:
                result.append(l)
        return result

