class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res = []
        new_start, new_end = newInterval

        for i in range(len(intervals)):
            start, end = intervals[i]

            # 1. Current interval is completely before newInterval
            if end < new_start:
                res.append([start, end])

            # 2. Current interval is completely after newInterval
            elif start > new_end:
                res.append([new_start, new_end])
                # add rest of intervals and return
                return res + intervals[i:]

            # 3. Overlap -> merge newInterval
            else:
                new_start = min(new_start, start)
                new_end = max(new_end, end)

        # if newInterval wasn't added yet (it goes at the end)
        res.append([new_start, new_end])
        return res