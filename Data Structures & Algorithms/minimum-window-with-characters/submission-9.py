class Solution:
    def minWindowNaive(self, s: str, t: str) -> str:
        counterT = defaultdict(int)
        counterS = defaultdict(int)
        
        for ch in t:
            counterT[ch] += 1
        
        l, r = 0, 0
        min_length = float("inf")
        min_seq = ""

        while r < len(s):
            counterS[s[r]] += 1
            while self.is_valid(counterS, counterT):
                if (r - l + 1) < min_length:
                    min_length = (r - l + 1)
                    min_seq = s[l: r + 1]

                counterS[s[l]] -= 1
                l += 1
            r += 1

        return min_seq
        
    def is_valid(self, counterS, counterT):
        for k, v in counterT.items():
            if not(k in counterS and counterS[k] >= v):
                return False

        return True

    def minWindow(self, s: str, t: str) -> str:
        counterT = defaultdict(int)
        counterS = defaultdict(int)

        for ch in t:
            counterT[ch] += 1

        l, r = 0, 0
        min_length = float("inf")
        min_seq = [l, r]
        have, need = 0, len(counterT)

        while r < len(s):
            counterS[s[r]] += 1

            if s[r] in counterT and counterS[s[r]] == counterT[s[r]]:
                have += 1

            while have == need:
                if (r - l + 1) < min_length:
                    min_length = (r - l + 1)
                    min_seq = [l, r]


                counterS[s[l]] -= 1
                if s[l] in counterT and counterS[s[l]] < counterT[s[l]]:
                    have -= 1
                l += 1

            r += 1

        l, r = min_seq
        return s[l: r + 1] if min_length != float("inf") else ""


    