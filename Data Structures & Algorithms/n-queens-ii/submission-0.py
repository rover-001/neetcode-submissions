class Solution:
    def totalNQueens(self, n: int) -> int:
        count = 0
        cols = set()

        diag1 = set()
        diag2 = set()

        def backtrack(row):

            if row == n:
                return 1

            total = 0

            for col in range(n):

                if col in cols:
                    continue

                if row - col in diag1:
                    continue

                if row + col in diag2:
                    continue

                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                total += backtrack(row + 1)

                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

            return total

        return backtrack(0)