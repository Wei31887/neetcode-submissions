class Solution:

    prefix = '#'

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        encode_string = []
        for s in strs:
            encode_string.append(str(len(s)) + self.prefix + s)
        return "".join(encode_string)

    def decode(self, s: str) -> List[str]:
        
        decode_string = []

        l = 0
        while l < len(s):
            r = l
            while s[r] != self.prefix:
                r += 1

            count = int(s[l : r])
            content = s[r + 1 : r + 1 + count]
            decode_string.append(content)

            l = r + 1 + count

        return decode_string
