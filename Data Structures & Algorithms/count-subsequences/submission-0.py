class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        res = []

        def backtracking(i, seq):
            if len(seq) == len(t) and seq == t:
                res.append(seq)
                return

            if i == len(s):
                return

            seq += s[i]
            backtracking(i + 1, seq)
            seq = seq[:-1]

            backtracking(i + 1, seq)

        backtracking(0, "")
    
        return len(res)
    