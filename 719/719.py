from typing import List

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def merge_and_count(left: List[int], right: List[int]) -> (int, List[int]):
 
            count = 0
            merged = []
            i, j = 0, 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
                    count += len(left) - i

            merged.extend(left[i:])
            merged.extend(right[j:])
            return count, merged

        def sort_and_count(arr: List[int]) -> (int, List[int]):

            if len(arr) <= 1:
                return 0, arr

            mid = len(arr) // 2
            left_count, left_sorted = sort_and_count(arr[:mid])
            right_count, right_sorted = sort_and_count(arr[mid:])
            merge_count, sorted_arr = merge_and_count(left_sorted, right_sorted)

            return left_count + right_count + merge_count, sorted_arr

        def count_pairs_with_distance(max_dist: int) -> int:

            count = 0
            j = 0
            for i in range(len(nums)):
                while j < len(nums) and nums[j] - nums[i] <= max_dist:
                    j += 1
                count += j - i - 1
            return count

 
        nums.sort()


        low, high = 0, nums[-1] - nums[0]
        while low < high:
            mid = (low + high) // 2
            if count_pairs_with_distance(mid) < k:
                low = mid + 1
            else:
                high = mid

        return low

####################
def main():
    solucao = Solution()

    # Teste 1: Saída esperada: 2
    nums1 = [1, 3, 1]
    k1 = 1
    print(solucao.smallestDistancePair(nums1, k1))

    # Teste 2: Saída esperada: 0
    nums2 = [1, 1, 1]
    k2 = 2
    print(solucao.smallestDistancePair(nums2, k2))

    # Teste 3: Saída esperada: 3
    nums3 = [1, 6, 1]
    k3 = 3
    print(solucao.smallestDistancePair(nums3, k3))

main()