class Solution:
    def toLowerCase(self, s: str) -> str:
        res=[]
        for c in s:
            if 'A'<=c<='Z':
                res.append(chr(ord(c)+32))
            else:
                res.append(c)
        return "".join(res)