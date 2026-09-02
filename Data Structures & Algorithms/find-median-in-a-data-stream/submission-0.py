import heapq

class MedianFinder:

    def __init__(self):
        self.lower_half = []
        self.upper_half = []
        

    def addNum(self, num: int) -> None:
        if not self.lower_half or num <= -self.lower_half[0]:
            heapq.heappush(self.lower_half, -num)
        else:
            heapq.heappush(self.upper_half, num)

        if len(self.lower_half) > len(self.upper_half) + 1:
            val = heapq.heappop(self.lower_half)
            heapq.heappush(self.upper_half, -val)
        elif len(self.upper_half) > len(self.lower_half):
            val = heapq.heappop(self.upper_half)
            heapq.heappush(self.lower_half, -val)


        

    def findMedian(self) -> float:
        isOdd = (len(self.lower_half) + len(self.upper_half)) % 2 != 0
        if isOdd:
            return -self.lower_half[0]
        else:
            return (-self.lower_half[0] + self.upper_half[0]) / 2
        
        