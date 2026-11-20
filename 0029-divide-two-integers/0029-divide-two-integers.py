class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Overflow case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Work with negatives to avoid overflow, result sign
        negative = (dividend < 0) != (divisor < 0)

        dividend = -abs(dividend)
        divisor = -abs(divisor)

        quotient = 0

        # Subtract divisor * 2^k as much as possible
        while dividend <= divisor:
            temp = divisor
            multiple = 1
            # Double temp while it still fits
            while dividend <= (temp << 1) and (temp << 1) < 0:
                temp <<= 1
                multiple <<= 1

            dividend -= temp
            quotient += multiple

        if negative:
            quotient = -quotient

        return max(INT_MIN, min(INT_MAX, quotient))