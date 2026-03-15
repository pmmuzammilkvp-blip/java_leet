class Solution:
    def merge(self, intervals):
        if not intervals:
            return []

        # Sort intervals by start time
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        for current in intervals[1:]:
            prev = merged[-1]

            if current[0] <= prev[1]:  # Overlap
                prev[1] = max(prev[1], current[1])  # Merge
            else:
                merged.append(current)

        return merged
