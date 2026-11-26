class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = []
        if not matrix:
            return res

        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # 1. Left -> Right (top row)
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            top += 1

            # 2. Top -> Bottom (right column)
            for row in range(top, bottom + 1):
                res.append(matrix[row][right])
            right -= 1

            # 3. Right -> Left (bottom row)
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    res.append(matrix[bottom][col])
                bottom -= 1

            # 4. Bottom -> Top (left column)
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    res.append(matrix[row][left])
                left += 1

        return res