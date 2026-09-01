class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = []

        for s in strs:
            ans.append('#')
            ans.append(str(len(s)))
            ans.append('#')
            ans.append(s)

        return ''.join(ans)


    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0

        while i < len(s):
            i += 1              # skip first #

            j = i
            while s[j] != '#':
                j += 1

            length = int(s[i:j])

            i = j + 1           # start of actual string
            string = s[i:i + length]

            ans.append(string)

            i += length

        return ans