class Solution:

    def checkValidString2(self, s: str) -> bool:
        memo = {}  # Diccionario para memoización: (i, openP) -> True/False

        def dfs(i, openP) -> bool:
            # openP = número de "(" abiertos pendientes por cerrar

            # ❌ Si tenemos más ")" que "(", ya no es válido
            if openP < 0:
                return False

            # 🎯 Caso base: llegamos al final del string
            # Solo es válido si todos los "(" fueron cerrados
            if i == len(s):
                return openP == 0

            # ⚡ Si ya resolvimos este estado, lo reutilizamos
            if (i, openP) in memo:
                return memo[(i, openP)]

            # 🔍 Exploramos dependiendo del caracter actual
            if s[i] == "*":
                # "*" puede ser:
                # 1. "(" → incrementa openP
                # 2. ")" → decrementa openP
                # 3. "" (vacío) → no cambia openP
                result = (
                    dfs(i + 1, openP + 1) or   # usar "*" como "("
                    dfs(i + 1, openP - 1) or   # usar "*" como ")"
                    dfs(i + 1, openP)          # ignorar "*"
                )
            else:
                if s[i] == "(":
                    # Abrimos un paréntesis
                    result = dfs(i + 1, openP + 1)
                elif s[i] == ")":
                    # Cerramos un paréntesis
                    result = dfs(i + 1, openP - 1)

            # 💾 Guardamos el resultado en memo
            memo[(i, openP)] = result

            return result  # ✅ IMPORTANTE: regresar el resultado

        return dfs(0, 0)

    def checkValidString(self, s: str) -> bool:
        memo = {}
        def dfs(i, openP):
            if openP < 0:
                return False
            
            if i == len(s):
                return openP == 0
            
            if (i, openP) in memo:
                return memo[(i, openP)]

            if s[i] == "(":
                res = dfs(i + 1, openP + 1)
            elif s[i] == ")":
                res = dfs(i + 1, openP - 1)
            elif s[i] == "*":
                res = (
                    dfs(i + 1, openP + 1) or
                    dfs(i + 1, openP - 1) or
                    dfs(i + 1, openP)
                )
            
            memo[(i, openP)] = res
            return res

        return dfs(0, 0)

