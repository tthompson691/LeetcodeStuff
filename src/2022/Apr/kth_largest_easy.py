from wrappers import time_it
import heapq

class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.nums=nums
        heapq.heapify(self.nums)
        
        while len(self.nums) > k:
            heapq.heappop(self.nums)
    
    def add(self, val):
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.heap)
        
        return self.nums[0]


if __name__ == "__main__":
    k = 3
    nums = [4, 5, 8, 2]
    
    obj = KthLargest(k, nums)
    
    num_stream = [3, 5, 10, 9, 4]
    ans = []
    for num in num_stream:
        param_1 = obj.add(num)
        ans.append(param_1)
        
    ans