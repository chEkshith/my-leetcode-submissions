class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        zero = ord('0') 

        while i >= 0 or j >= 0 or carry:
            sum_val = carry

            if i >= 0:
                sum_val += ord(a[i]) - zero 
                i -= 1
            if j >= 0:
                sum_val += ord(b[j]) - zero
                j -= 1

            res.append(chr((sum_val % 2) + zero)) 
            carry = sum_val // 2

        return ''.join(res[::-1])