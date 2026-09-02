class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)

        left = []
        right = []

        # Add first candidates
        left_end = min(candidates, n)

        for i in range(left_end):
            heapq.heappush(left, costs[i])

        # Add last candidates without overlapping
        right_start = max(candidates, n - candidates)

        for i in range(right_start, n):
            heapq.heappush(right, costs[i])

        # Pointers to workers not yet added to heaps
        l = left_end
        r = right_start - 1

        total = 0

        for _ in range(k):

            if not right or (left and left[0] <= right[0]):
                # Hire from left
                total += heapq.heappop(left)

                if l <= r:
                    heapq.heappush(left, costs[l])
                    l += 1

            else:
                # Hire from right
                total += heapq.heappop(right)

                if l <= r:
                    heapq.heappush(right, costs[r])
                    r -= 1

        return total