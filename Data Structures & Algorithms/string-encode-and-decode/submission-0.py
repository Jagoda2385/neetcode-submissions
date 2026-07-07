class Solution:

    def encode(self, strs: List[str]) -> str:
        lenstrs = []
        for string in strs:
            lenstrs.append(len(string))
        joined = "".join(strs)

    def decode(self, s: str) -> List[str]:
        output = []
        for i in range(len(lenstrs)):
            for j in range(0, j <= lenstrs[i], len(joined)):
                output.append(joined[j:lenstrs[i]])


