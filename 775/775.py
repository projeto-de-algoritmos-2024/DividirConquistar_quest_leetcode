from typing import List

class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        

        def merge_and_count(arr: List[int], left: int, mid: int, right: int) -> int:
            temp = []
            i, j = left, mid + 1
            inversions = 0
            
            while i <= mid and j <= right:
                if arr[i] <= arr[j]:
                    temp.append(arr[i])
                    i += 1
                else:
                    temp.append(arr[j])
                    j += 1
                    inversions += (mid - i + 1) 
            
            temp.extend(arr[i:mid + 1])
            temp.extend(arr[j:right + 1])
            arr[left:right + 1] = temp
            return inversions
        
  
        def merge_sort(arr: List[int], left: int, right: int) -> int:
            if left >= right:
                return 0
            mid = (left + right) // 2
            inv_count = merge_sort(arr, left, mid)
            inv_count += merge_sort(arr, mid + 1, right)
            inv_count += merge_and_count(arr, left, mid, right)
            return inv_count
        
 
        def count_local(arr: List[int]) -> int:
            local_inversions = 0
            for i in range(1, len(arr)):
                if arr[i] < arr[i - 1]:
                    local_inversions += 1
            return local_inversions
        

        local_inversions = count_local(nums)
        

        global_inversions = merge_sort(nums[:], 0, len(nums) - 1) 
        

        return local_inversions == global_inversions

####################
def main():
    solucao = Solution()

    # Teste 1: Saída esperada: True (todas as inversões são locais)
    nums1 = [1, 2, 0]
    print(solucao.isIdealPermutation(nums1))  # True

    # Teste 2: Saída esperada: False (existe uma inversão global não local)
    nums2 = [1, 0, 2]
    print(solucao.isIdealPermutation(nums2))  # False

    # Teste 3: Saída esperada: True (não há inversões)
    nums3 = [0, 1, 2]
    print(solucao.isIdealPermutation(nums3))  # True

    # Teste 4: Teste com uma inversão global não local
    nums4 = [2, 0, 1]
    print(solucao.isIdealPermutation(nums4))  # False

main()