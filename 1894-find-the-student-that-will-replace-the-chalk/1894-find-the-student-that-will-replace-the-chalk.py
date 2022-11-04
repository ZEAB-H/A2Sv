class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        s = sum(chalk)
        k %= s
        n = len(chalk)
        for i in range(n):
            if chalk[i]>k:
                return i
            k -= chalk[i]
        