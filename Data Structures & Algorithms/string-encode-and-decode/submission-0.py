class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            length = len(s)
            res += str(length) + "#" + s

        return res


    def decode(self, s: str) -> List[str]:
        res = []
        delim = "#"
        i = 0
        length = ""

        while i < len(s):
            if s[i] == delim:
                str_len = int(length)
                length = ""
                i += 1

                string = s[i : i+str_len]
                res.append(string)
                i += str_len

            else:
                length += s[i]
                i += 1
            
        return res