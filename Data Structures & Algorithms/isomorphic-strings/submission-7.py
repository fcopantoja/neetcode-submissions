class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapST, mapTS = {}, {}

        for s1, t1 in zip(s, t):
            if (
                (s1 in mapST and mapST[s1] != t1) or
                (t1 in mapTS and mapTS[t1] != s1)
            ):
                return False

            mapST[s1] = t1
            mapTS[t1] = s1

        return True