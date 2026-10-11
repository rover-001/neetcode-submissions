
from collections import Counter
import heapq
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        max_heap = [-count for count in counts.values()]
        heapq.heapify(max_heap)

        cycles = 0

        while max_heap:
            temp = []
            task_count = 0

            for _ in range(n + 1):
                if max_heap:
                    count = heapq.heappop(max_heap)
                    task_count += 1

                    if count + 1 < 0:
                        temp.append(count + 1)

            for count in temp:
                heapq.heappush(max_heap, count)

            cycles += task_count if not max_heap else n + 1

        return cycles
