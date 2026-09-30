class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals:
            return []

        # 1. Sort by start time
        intervals.sort(key=lambda x: x[0])

        merged = [intervals[0]]

        for start, end in intervals[1:]:
            last_end = merged[-1][1]

            # 2. Overlap? -> merge
            if start <= last_end:
                merged[-1][1] = max(last_end, end)
            # 3. No overlap -> new interval
            else:
                merged.append([start, end])

        return merged