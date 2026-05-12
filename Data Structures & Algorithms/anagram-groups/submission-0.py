class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_map=dict()

        for i in strs:
            sorted_str=''.join(sorted(i))
            if sorted_str in final_map:
                final_map[sorted_str].append(i)
            else:
                final_map[sorted_str]=[]
                final_map[sorted_str].append(i)
        ans=[]
        for i in final_map:
            ans.append(final_map.get(i, []))

        return ans