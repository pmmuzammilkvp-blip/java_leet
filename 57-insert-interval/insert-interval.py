class Solution:
    def insert(self, intervals, newInterval):
        if not newInterval:
            return intervals  # Edge case: no new interval

        merged = []
        i = 0
        n = len(intervals)

        # Add all intervals ending before newInterval starts
        while i < n and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i += 1

        # Merge overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        # Add the merged interval
        merged.append(newInterval)

        # Add remaining intervals
        while i < n:
            merged.append(intervals[i])
            i += 1

        return merged
