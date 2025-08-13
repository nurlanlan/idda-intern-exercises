class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def backtrack(cur: list[str], open_cnt: int, close_cnt: int):
            if open_cnt == n and close_cnt == n:
                res.append("".join(cur))
                return

            if open_cnt < n:
                cur.append("(")
                backtrack(cur, open_cnt + 1, close_cnt)
                cur.pop()

            if close_cnt < open_cnt:
                cur.append(")")
                backtrack(cur, open_cnt, close_cnt + 1)
                cur.pop()

        backtrack([], 0, 0)
        return res
