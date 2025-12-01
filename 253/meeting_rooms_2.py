class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = []
        end = []

        for s, e in intervals:
            start.append(s)
            end.append(e)
        
        sort_start = sorted(start)
        sort_end = sorted(end)

        count = 0
        max_count = 0

        s = 0
        e = 0

        while s < len(sort_start):
            if sort_start[s] < sort_end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            
            max_count = max(count, max_count)
        
        return max_count