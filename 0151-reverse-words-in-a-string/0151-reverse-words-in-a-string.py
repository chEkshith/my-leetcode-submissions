class Solution:
    def reverseWords(self, s: str) -> str:
        # Split by whitespace (automatically handles multiple spaces)
        words = s.split()
        # Reverse the word order
        words.reverse()
        # Join with a single space
        return " ".join(words)
