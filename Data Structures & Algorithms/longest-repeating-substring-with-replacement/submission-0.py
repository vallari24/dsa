class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        maxcount = 0

        for l in range(n):
            for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                replacements = 0
                r = l

                while r < n:
                    if s[r] != char:
                        replacements += 1

                    if replacements > k:
                        break

                    r += 1

                maxcount = max(maxcount, r - l)

        return maxcount