class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for char in columnTitle:
            # A=1, B=2 ... Z=26
            # Shift previous result by 26 and add current
            result = result * 26 + (ord(char) - ord('A') + 1)
        return result