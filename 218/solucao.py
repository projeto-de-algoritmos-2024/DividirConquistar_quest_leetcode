from typing import List

class Solution:
    def getSkyline(self, edificios: List[List[int]]) -> List[List[int]]:

        def mescla(esquerda: List[List[int]], direita: List[List[int]]) -> List[List[int]]:
            
            esq = len(esquerda)
            dir = len(direita)
            resultado = []
            he, hd, i, j, ultima_altura = 0, 0, 0, 0, 0

            while i < esq and j < dir:
                if esquerda[i][0] < direita[j][0]:
                    x, he = esquerda[i]
                    i += 1

                elif esquerda[i][0] > direita[j][0]:
                    x, hd = direita[j]
                    j += 1

                else:
                    x, he = esquerda[i]
                    _, hd = direita[j]
                    i += 1
                    j += 1

                hMax = max(he, hd)

                if hMax != ultima_altura:
                    resultado.append([x, hMax])
                    ultima_altura = hMax 

            for item in esquerda[i:]:
                resultado.append(item)

            for item in direita[j:]:
                resultado.append(item)

            return resultado

        def divide(edificios: List[List[int]]) -> List[List[int]]:
            if not edificios:
                return []
    
            elif len(edificios) == 1:
                x_inicio, x_fim, altura = edificios[0]
                return [[x_inicio, altura], [x_fim, 0]]
            
            else:
                meio = len(edificios) // 2
                esquerda = divide(edificios[:meio])
                direita = divide(edificios[meio:])
                return mescla(esquerda, direita)

        return divide(edificios)


####################
def main():
    solucao = Solution()

    # Saída: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
    result = solucao.getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]])
    print(result)

    # Saída: [[0,3],[5,0]]
    result = solucao.getSkyline([[0,2,3],[2,5,3]])
    print(result)

main()
####################