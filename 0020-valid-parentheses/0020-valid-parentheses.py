class Solution:
    def isValid(self, s: str) -> bool:
        #Implementation using stack and hashmap;
        stack=[]
        mapp={')':'(','}':'{',']':'['}
        for char in s:
            if char in mapp.values():
                stack.append(char)
            elif char in mapp.keys():
                if not stack or stack.pop()!=mapp[char]:
                    return False
        return not stack
        