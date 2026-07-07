class Solution:
    def encode(self, strs: List[str]) -> str:
        return "###".join(strs)

    def decode(self, s: str) -> List[str]:
        output = []
        number = 0
        for i in range(len(s)):
            if s[i] == '###':
                output.append(s[number:i])
                number = i + 1
        output.append(s[number:])   
        return output