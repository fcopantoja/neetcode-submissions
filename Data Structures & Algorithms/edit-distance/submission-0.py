class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Vamos a construir una matriz DP donde:
        # matrix[i][j] representa la distancia mínima de edición
        # entre word1[i:] y word2[j:]
        
        # Creamos la matriz con tamaño (len(word1)+1) x (len(word2)+1)
        matrix = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        # Caso base 1:
        # Si word2 ya se terminó (j == len(word2)),
        # necesitamos eliminar todos los caracteres restantes de word1
        for i in range(len(word1) + 1):
            matrix[i][-1] = len(word1) - i

        # Caso base 2:
        # Si word1 ya se terminó (i == len(word1)),
        # necesitamos insertar todos los caracteres restantes de word2
        for j in range(len(word2) + 1):
            matrix[-1][j] = len(word2) - j
        
        # Llenamos la matriz de abajo hacia arriba (bottom-up)
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                
                # Si los caracteres coinciden, no hay costo adicional
                if word1[i] == word2[j]:
                    matrix[i][j] = matrix[i + 1][j + 1]
                else:
                    # Si no coinciden, consideramos las 3 operaciones:
                    # 1. Insertar (movernos en word2): matrix[i][j+1]
                    # 2. Reemplazar (movernos en ambos): matrix[i+1][j+1]
                    # 3. Eliminar (movernos en word1): matrix[i+1][j]
                    matrix[i][j] = 1 + min(
                        matrix[i][j + 1],      # insertar
                        matrix[i + 1][j + 1],  # reemplazar
                        matrix[i + 1][j]       # eliminar
                    )
        
        # El resultado final está en matrix[0][0],
        # que representa transformar todo word1 en todo word2
        return matrix[0][0]