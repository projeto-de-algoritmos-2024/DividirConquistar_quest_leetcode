from typing import List

class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        def k_esimoMenor(numsIndices, k):

            menor, igual, maior = [], [], []

            if len(numsIndices) <= 5:
                return sorted(numsIndices)[k - 1]
            
            grupos = [numsIndices[i:i + 5] for i in range(0, len(numsIndices), 5)]
            medianas = [sorted(grupo)[len(grupo) // 2] for grupo in grupos]

            pivo = k_esimoMenor(medianas, len(medianas) // 2 + 1)
            
            for num in numsIndices:
                if num < pivo:
                    menor.append(num)
                elif num == pivo:
                    igual.append(num)
                else:
                    maior.append(num)
            
            if k <= len(menor):
                return k_esimoMenor(menor, k)
            elif k <= len(menor) + len(igual):
                return igual[k - len(menor) - 1]
            else:
                return k_esimoMenor(maior, k - len(menor) - len(igual))
        
        result = []
        for ki, trimi in queries:
            truncado = [(num[-trimi:], j) for j, num in enumerate(nums)]
            kth = k_esimoMenor(truncado, ki)
            result.append(kth[1])
        
        return result


def main():
    nums1 = ["24", "37", "96", "04"]
    queries1 = [[2, 1], [2, 2]]
    # Saída [3, 0]
    
    nums2 = ["102", "473", "251", "814"]
    queries2 = [[1, 1], [2, 3], [4, 2], [1, 2]]
    # Saída [2, 2, 1, 0]

    solution = Solution()
    
    output1 = solution.smallestTrimmedNumbers(nums1, queries1)
    print(output1)
    
    output2 = solution.smallestTrimmedNumbers(nums2, queries2)
    print(output2)

main()