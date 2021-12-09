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

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len_1 = len(nums1)
        len_2 = len(nums2)
        if len_1 > len_2:
            return self.findMedianSortedArrays(nums2, nums1)
        
        total = len_1 + len_2
        low = 0
        high = len_1
        
        while low <= high:
            mid_1 = low + int((high - low)/2)
            mid_2 = int(total/2) - mid_1
            
            l1 = nums1[mid_1 - 1] if mid_1 != 0 else -999999
            r1 = nums1[mid_1] if mid_1 != len_1 else 999999
            
            l2 = nums2[mid_2 - 1] if mid_2 != 0 else -999999
            r2 = nums2[mid_2] if mid_2 != len_2 else 999999
            
            if l1 <= r2 and l2 <= r1:
                if total % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2
                return min(r1, r2)
            elif l1 > r2:
                high = mid_1 - 1
            else:
                low = mid_1 + 1
        
        return -1