class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        a = dict()
        for i in s:
            if i in a:
                a[i]+=1
            else:
                a[i]=1
        for i in t:
            if i in a:
                a[i]-=1
            else:
                return False
        for i in a:
            if a[i]!=0:
                return False
        return True

        