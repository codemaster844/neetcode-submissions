class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniqueSet=set()
        left=0
        right=0
        maxLen=0

        while right < len(s):
            if s[right] not in uniqueSet:
                uniqueSet.add(s[right])
                maxLen=max(maxLen,right-left+1)
                right+=1
            else:
                uniqueSet.remove(s[left])
                left+=1
        return maxLen




        