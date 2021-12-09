class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currSet = set(s)
        if len(currSet) == 0:
            return 0
        elif len(currSet) == 1:
            return 1
        
        charWindow = []
        start = 0
        end = 0
        maxLen = 0
        
        for c in s:
            if c not in charWindow:
                charWindow.append(c)
                end += 1
                maxLen = max(end - start, maxLen)
            else:
                while c in charWindow:
                    charWindow.remove(s[start])
                    start += 1
                charWindow.append(c)
                end += 1
            if maxLen == len(currSet):
                return maxLen
            
        return maxLen