
import heapq
from typing import List

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)

        sorted_tasks = sorted(
            (enqueue, processing, i)
            for i, (enqueue, processing) in enumerate(tasks)
        )

        min_heap = []
        result = []
        time = 0
        i = 0

        while i < n or min_heap:
            if not min_heap and time < sorted_tasks[i][0]:
                time = sorted_tasks[i][0]

            while i < n and sorted_tasks[i][0] <= time:
                enqueue, processing, index = sorted_tasks[i]
                heapq.heappush(min_heap, (processing, index))
                i += 1

            processing, index = heapq.heappop(min_heap)
            result.append(index)
            time += processing

        return result
