class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Guardamos la última posición donde aparece cada carácter
        hmap = defaultdict(int)
        for i in range(len(s)):
            hmap[s[i]] = i
        
        size = 0   # tamaño de la partición actual
        end = 0    # límite actual de la partición
        result = []

        for i, c in enumerate(s):
            size += 1

            # Extendemos el límite si este carácter aparece más adelante
            if hmap[c] > end:
                end = hmap[c]

            # Si llegamos al límite, cerramos la partición
            if i == end:
                result.append(size)
                size = 0  # reiniciamos para la siguiente partición
        
        return result