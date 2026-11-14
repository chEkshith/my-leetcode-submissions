class Solution:
    def countAndSay(self, n: int) -> str:
        current = "1"
        
        for _ in range(n - 1):
            next_seq = []
            i = 0
            
            while i < len(current):
                count = 1
                # Count consecutive identical characters
                while i + 1 < len(current) and current[i] == current[i + 1]:
                    count += 1
                    i += 1
                
                # Append the count and the digit
                next_seq.append(str(count))
                next_seq.append(current[i])
                i += 1
                
            current = "".join(next_seq)
            
        return current
