class Solution(object):
    maxSize = 0
    def lengthOfLongestSubstring(self, s):
        size = 0 
        tbl = {}
        currMaxIdx= 0

        for idx  in range(0, len(s)):
            if s[idx] in tbl:
                currMaxIdx = max(tbl[s[idx]], currMaxIdx)
            
            self.maxSize = max(self.maxSize, idx - currMaxIdx + 1)
            tbl[s[idx]]=idx + 1


        return self.maxSize


S = "dvdf"
sol = Solution()
print (sol.lengthOfLongestSubstring(S))