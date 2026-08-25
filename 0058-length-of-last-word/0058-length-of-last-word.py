class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # split() without arguments handles any whitespace and 
        # ignores leading/trailing spaces automatically.
        words = s.split()
        
        if not words:
            return 0
            
        return len(words[-1])