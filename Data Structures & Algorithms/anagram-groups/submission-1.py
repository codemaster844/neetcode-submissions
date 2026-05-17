class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=defaultdict(list)

        for s in strs:
            charMap=[0]*26
            for i in s:
                charMap[ord(i)-ord('a')]+=1

            result[tuple(charMap)].append(s)
        return list(result.values())
        