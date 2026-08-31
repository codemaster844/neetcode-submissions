class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniqueSet=defaultdict(str)

        left=0
        right=0
        maxLen=0

        while right < len(s):
            if s[right] in uniqueSet:
                left=max(left,uniqueSet[s[right]]+1)
            uniqueSet[s[right]]=right
            maxLen=max(maxLen,right-left+1)
            right+=1

        return maxLen




        