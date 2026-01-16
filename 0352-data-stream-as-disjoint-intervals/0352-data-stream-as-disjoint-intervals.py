class SummaryRanges:

    def __init__(self):
        self.intervals = []

    def addNum(self, value: int) -> None:
        intervals = self.intervals
        n  = len(intervals)
        left, right = 0,n
        while left<right:
            mid = (left+right)//2
            if intervals[mid][0]<value:
                left = mid+1
            else:
                right = mid
        i = left
        start, end = value, value
        if i>0 and intervals[i-1][1]+1>= value:
            i-=1
            intervals[i][1] = max(intervals[i][1], value)
        elif i ==n or intervals[i][0]>value+1:
            intervals.insert(i,[value,value])
            return
        else:
            intervals[i][0] = min(intervals[i][0], value)
            intervals[i][1] = max(intervals[i][1], value)
        while i+1< len(intervals) and intervals[i][1]+1>=intervals[i+1][0]:
            intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
            intervals.pop(i+1)
        


    def getIntervals(self) -> List[List[int]]:
        return self.intervals


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()