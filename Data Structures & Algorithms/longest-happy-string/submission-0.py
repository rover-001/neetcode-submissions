
import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []

        for count, char in [(a, 'a'), (b, 'b'), (c, 'c')]:
            if count > 0:
                heapq.heappush(heap, (-count, char))

        result = []

        while heap:
            count, char = heapq.heappop(heap)

            # Cannot use this character three times consecutively
            if len(result) >= 2 and result[-1] == result[-2] == char:
                if not heap:
                    break

                # Use the next most frequent character instead
                second_count, second_char = heapq.heappop(heap)
                result.append(second_char)
                second_count += 1  # One occurrence used

                if second_count < 0:
                    heapq.heappush(heap, (second_count, second_char))

                # Restore the original character for later
                heapq.heappush(heap, (count, char))

            else:
                result.append(char)
                count += 1  # One occurrence used

                if count < 0:
                    heapq.heappush(heap, (count, char))

        return ''.join(result)
