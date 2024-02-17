# Intuition
The problem involves finding the furthest building you can reach given a certain number of bricks and ladders. You can use ladders to bypass tall buildings, and if you don't have enough ladders, you can use bricks to climb instead. The intuition here is to simulate the process of climbing using a priority queue (min heap) to keep track of the heights of the buildings you need to climb. 

# Approach
1. Initialize a min heap to keep track of the height differences between adjacent buildings.
2. Iterate through the buildings, calculating the height difference between each pair of adjacent buildings.
3. If the height difference is non-negative, meaning you can climb without using any resources, ignore it.
4. If the height difference is positive, push it onto the heap.
5. If the size of the heap exceeds the number of ladders you have, pop the smallest height difference from the heap and subtract it from the available bricks.
6. If at any point you run out of bricks, return the index of the building you're currently at.
7. If you reach the end of the buildings without running out of resources, return the index of the last building.

# Complexity
- Time complexity: 
  - Building the heap: O(nlogk), where n is the number of buildings and k is the number of ladders.
  - Iterating through the buildings: O(n)
  - Overall time complexity: O(nlogk)
- Space complexity:
  - Heap space: O(k), where k is the number of ladders.
  - Overall space complexity: O(k)

# Code
```python
from typing import List
from heapq import heappush, heappop

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        heap = []
        
        for i in range(n-1):
            h = heights[i+1] - heights[i]
            if h <= 0:
                continue
            heappush(heap, h)
            if len(heap) > ladders:
                min_h = heappop(heap)
                bricks -= min_h
            if bricks < 0:
                return i
        return n - 1
```
