class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)

        if total % k != 0:
            return False

        target = total // k
        nums.sort(reverse=True)

        if nums[0] > target:
            return False

        used = [False] * len(nums)

        def backtrack(start, buckets_left, subset_sum):
            if buckets_left == 0:
                return True

            if subset_sum == target:
                return backtrack(0, buckets_left - 1, 0)

            prev = -1

            for j in range(start, len(nums)):
                if used[j] or nums[j] == prev:
                    continue

                if subset_sum + nums[j] > target:
                    continue

                used[j] = True

                if backtrack(j + 1, buckets_left, subset_sum + nums[j]):
                    return True

                used[j] = False
                prev = nums[j]

                # If this number cannot start a bucket, trying other
                # numbers as the first element is equivalent.
                if subset_sum == 0:
                    break

            return False

        return backtrack(0, k, 0)