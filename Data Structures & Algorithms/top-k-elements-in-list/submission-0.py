class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        elemetsCounts=Counter(nums)
        freqList=defaultdict(list)
        for i,j in elemetsCounts.items():
            freqList[j].append(i)
        for i in range(len(nums),-1,-1):
            for j in freqList[i]:
                ans.append(j)
                if len(ans)==k:
                    return ans
        